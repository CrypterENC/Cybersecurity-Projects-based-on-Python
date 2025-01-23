import mysql.connector

from rich import print as printc
from rich.console import Console
console = Console()

def dbconfig():
    try:
        database = mysql.connector.connect(
            host="localhost",
            user='root',
            password='root@kali'
        )
    except Exception as e:
        printc("[red][!] An error occurred while connecting to the database. Please check your database configuration and try again. [/red]")
        console.print_exception(show_locals=True)

    return database