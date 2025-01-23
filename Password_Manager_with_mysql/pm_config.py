import sys
import getpass
import hashlib
import random
import string

from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console

console = Console()


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

                                  .aMMMb    .aMMMb     dMMMMb     dMMMMMP     dMP    .aMMMMP    dMP dMP     dMMMMb     .aMMMb  dMMMMMMP    .aMMMb     dMMMMb 
                                 dMP"VMP   dMP"dMP    dMP dMP    dMP         amr    dMP"       dMP dMP     dMP.dMP    dMP"dMP    dMP      dMP"dMP    dMP.dMP 
                                dMP       dMP dMP    dMP dMP    dMMMP       dMP    dMP MMP"   dMP dMP     dMMMMK"    dMMMMMP    dMP      dMP dMP    dMMMMK"  
                               dMP.aMP   dMP.aMP    dMP dMP    dMP         dMP    dMP.dMP    dMP.aMP     dMP"AMF    dMP dMP    dMP      dMP.aMP    dMP"AMF   
                               VMMMP"    VMMMP"    dMP dMP    dMP         dMP     VMMMP"     VMMMP"     dMP dMP    dMP dMP    dMP       VMMMP"    dMP dMP    

"""

def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))

def config():
    print(logo)
    db = dbconfig()
    cursor = db.cursor()
    
    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        if e.errno == 1007:
            printc("[red][!] Database 'pm' already exists.")
            db.close()
            sys.exit(0)
        else:
            printc("[red][!] An error occurred while trying to create db.")
            console.print_exception(show_locals=True)
            sys.exit(0)
            
    printc("[green][+][/green] Database 'pm' created successfully.")

    # Create tables
    query = "CREATE TABLE pm.secrets (masterkey_hash TEXT NOT NULL, devices_secret TEXT NOT NULL)"
    res =cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created successfully.")

    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created successfully.")

    mp=""
    while 1:
        master_key = getpass.getpass("Choose a MASTER PASSWORD: ")
        if master_key==getpass.getpass("Re-type: ") and master_key!="":
            break
        printc("[yellow][-] Please try again.[/yellow]")

    # Hash the MASTER PASSWORD
    hashed_master_key = hashlib.sha256(master_key.encode()).hexdigest()
    printc("[green][+][/green] Generated hash for MASTER PASSWORD.")

    # Generate a secret for devices
    device_secret = generateDeviceSecret()
    printc("[green][+][/green] Generated secret for devices.")

    # Add them to the database
    query = "INSERT INTO pm.secrets (masterkey_hash, devices_secret) VALUES (%s, %s)"
    val = (hashed_master_key, device_secret)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+][/green] Added to the database.")

    printc("[green][+] Configuration done![/green].")

    db.close()

config()