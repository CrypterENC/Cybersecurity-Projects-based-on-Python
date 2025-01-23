# Password Manager

A simple local password manager written in Python and using MySQL.

## Features

- Encrypts and stores passwords securely using AES encryption.
- Allows adding, listing, and searching for password entries.
- Requires a master password to access the password manager.

## Prerequisites

- Python 3.x
- MySQL server
- `mysql-connector-python` library (can be installed using `pip install mysql-connector-python`)
- `pycryptodome` library (can be installed using `pip install pycryptodome`)

## Installation

1. Clone the repository: ` https://github.com/CrypterENC/Cybersecurity-Projects-based-on-Python.git `.
2. Install the required dependencies: ` pip install -r requirements.txt `

### Mysql 
#### Install 

Download the latest version of Mysql [here](https://dev.mysql.com/downloads/installer/)

## Run

Run the configuration script: ` python .\pm_config.py `
- It will create the database and you just need to create MASTER PASSWORD.

### Usage
```
python password_mana.py -h
usage: password_manager [-h] [-s NAME] [-u URL] [-e EMAIL] [-l LOGIN] [-c] option

Description: Uses Mysql to store all the data

positional arguments:
  option                (a)dd / (e)xtract

optional arguments:
  -h, --help            show this help message and exit
  -s NAME, --name NAME  Site name
  -u URL, --url URL     Site URL
  -e EMAIL, --email EMAIL
                        Email
  -l LOGIN, --login LOGIN
                        Username
  -c                    Copy password to clipboard
```

### Add entry
```
python password_mana.pyy add -s site_name -u site_name.com -e mail@email.com -l username
```
### Retrieve entry
```
python password_mana.py extract
```
```
python password_mana.py e -s site_name
```
```
python password_mana.py e -s mysite -l myusername
```
```
python pm.py e -s site_name -l username --copy
```
