import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import sys

def encrypt(key, source, encode=True, keyType = 'hex'):
    source = source.encode()
    key = Random.new().read(AES.block_size) 
    IV = Random.new().read(AES.block_size)  
    cipher = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  
    source += bytes([padding]) * padding  
    data = IV + cipher.encrypt(source)  
    return base64.b64encode(key + data).decode() if encode else key + data

def decrypt(key, source, decode=True, keyType="hex"):
    source = source.encode()
    if decode:
        source = base64.b64decode(source)
    key = source[:AES.block_size]  
    data = source[AES.block_size:]  
    IV = data[:AES.block_size]  
    cipher = AES.new(key, AES.MODE_CBC, IV)
    data = cipher.decrypt(data[AES.block_size:]) 
    padding = data[-1] 
    if data[-padding:] != bytes([padding]) * padding: 
        raise ValueError("Invalid padding...")
    return data[:-padding] 

