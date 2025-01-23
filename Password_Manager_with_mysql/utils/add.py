import mysql.connector
from utils.dbconfig import dbconfig
import utils.aes
from getpass import getpass

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import base64

from rich import print as printc
from rich.console import Console

console = Console()

# compute masterkey
def computeMasterKey(master_password, device_secret):
    password = master_password.encode()
    salt = device_secret.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)
    return key    

# Check if an entry already exists
def checkEntry(sitename, siteurl, email, username):
    db = dbconfig()
    cursor = db.cursor()
    query = f"SELECT * FROM pm.entries WHERE sitename = '{sitename}' AND siteurl = '{siteurl}' AND email = '{email}' AND username = '{username}'"
    cursor.execute(query)
    results = cursor.fetchall()

    if len(results)!=0:
        return True
    return False

# Add an entry to the database
def addEntry(mp, ds, sitename, siteurl, email, username):
	# Check if the entry already exists
	if checkEntry(sitename, siteurl, email, username):
		printc("[yellow][-][/yellow] Entry with these details already exists")
		return

	# Input Password
	password = getpass("Password: ")

	# compute master key
	mk = computeMasterKey(mp,ds)

	# encrypt password with mk
	encrypted = utils.aes.encrypt(key=mk, source=password, keyType="bytes")

	# Add to db
	db = dbconfig()
	cursor = db.cursor()
	query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values (%s, %s, %s, %s, %s)"
	val = (sitename,siteurl,email,username,encrypted)
	cursor.execute(query, val)
	db.commit()

	printc("[green][+][/green] Added entry ")