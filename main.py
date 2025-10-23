#import & dependencies 
from cryptography.fernet import Fernet 
import json
import hashlib 
import os, sys 

#hashing 
def masterPasswordHash(masterPassword): 
    hash = haslib.sha256()
    sha256.update(masterPassword.encode())
    return sha256.hexdigest 

""" 
    SECURITY 
the majority of the encryption     
""" 


#encryption key 
def makeKey():
    return Fernet.generate_key()

#creates a cipher with the key 
def initCipher(key): 
    return Fernet(key)

#encrypts passwords 
def enryptPassword(cipher, password): 
    return cipher.encrypt(password.encode()).decode()

    # 

