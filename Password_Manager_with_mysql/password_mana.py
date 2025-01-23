import argparse
import hashlib
import pyperclip
import utils.add

from rich import print as printc
from getpass import getpass
from utils import retrive, generate
from utils.dbconfig import dbconfig

logo = """
    dMMMMb     .aMMMb    .dMMMb    .dMMMb    dMP dMP dMP    .aMMMb     dMMMMb     dMMMMb          
   dMP.dMP    dMP"dMP   dMP" VP   dMP" VP   dMP dMP dMP    dMP"dMP    dMP.dMP    dMP VMP          
  dMMMMP"    dMMMMMP    VMMMb     VMMMb    dMP dMP dMP    dMP dMP    dMMMMK"    dMP dMP           
 dMP        dMP dMP   dP .dMP   dP .dMP   dMP.dMP.dMP    dMP.aMP    dMP"AMF    dMP.aMP            
dMP        dMP dMP    VMMMP"    VMMMP"    VMMMPVMMP"     VMMMP"    dMP dMP    dMMMMP"             
                                                                                                  
                    dMMMMMMMMb     .aMMMb     dMMMMb     .aMMMb    .aMMMMP     dMMMMMP     dMMMMb 
                   dMP"dMP"dMP    dMP"dMP    dMP dMP    dMP"dMP   dMP"        dMP         dMP.dMP 
                  dMP dMP dMP    dMMMMMP    dMP dMP    dMMMMMP   dMP MMP"    dMMMP       dMMMMK"  
                 dMP dMP dMP    dMP dMP    dMP dMP    dMP dMP   dMP.dMP     dMP         dMP"AMF   
                dMP dMP dMP    dMP dMP    dMP dMP    dMP dMP    VMMMP"     dMMMMMP     dMP dMP                                                                                                    
"""

parser = argparse.ArgumentParser(description='Description: Uses Mysql to store all the data')

parser.add_argument('option', help='(a)dd / (e)xtract')
parser.add_argument("-s", "--name", help="Site name")
parser.add_argument("-u", "--url", help="Site URL")
parser.add_argument("-e", "--email", help="Email")
parser.add_argument("-l", "--login", help="Username")
parser.add_argument("-c", action='store_true', help='Copy password to clipboard')

args = parser.parse_args()

def inputAndValidateMasterPassword():
	mp = getpass("MASTER PASSWORD: ")
	hashed_master_password = hashlib.sha256(mp.encode()).hexdigest()
	db = dbconfig()
	cursor = db.cursor()
	query = "SELECT masterkey_hash, devices_secret FROM pm.secrets"
	cursor.execute(query)
	result = cursor.fetchall()[0]
	if hashed_master_password != result[0]:
		printc("[red][!] WRONG! [/red]")
		return None
	return [mp,result[1]]

def main():
	print(logo)
	if args.option in ["add","a"]:
		if args.name == None or args.url == None or args.login == None:
			if args.name == None:
				printc("[red][!][/red] Site Name (-s) required ")
			if args.url == None:
				printc("[red][!][/red] Site URL (-u) required ")
			if args.login == None:
				printc("[red][!][/red] Site Login (-l) required ")
			return
		if args.email == None:
			args.email = ""
		res = inputAndValidateMasterPassword()
		if res is not None:
			utils.add.addEntry(res[0],res[1],args.name,args.url,args.email,args.login)

	if args.option in ["extract","e"]:
		res = inputAndValidateMasterPassword()
		search = {}
		if args.name is not None:
			search["sitename"] = args.name
		if args.url is not None:
			search["siteurl"] = args.url
		if args.email is not None:
			search["email"] = args.email
		if args.login is not None:
			search["username"] = args.login
		if res is not None:
			utils.retrive.retriveEntries(res[0],res[1],search,decryptPassword = args.copy)
main()
