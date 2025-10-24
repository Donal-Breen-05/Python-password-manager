#import & dependencies 
from cryptography.fernet import Fernet 
import json
import hashlib 
import os, sys 

""" 
    SECURITY 
the majority of the encryption     
""" 

#hashing 
def masterPasswordHash(masterPassword): 
    hash = haslib.sha256()
    sha256.update(masterPassword.encode())
    return sha256.hexdigest 


#encryption key 
def makeKey():
    return Fernet.generate_key()

#creates a cipher with the key 
def initCipher(key): 
    return Fernet(key)

#encrypts passwords 
def enryptPassword(cipher, password): 
    return cipher.encrypt(password.encode()).decode()


""" 
    Users and User data 
the functions that take care of user data 
"""

def newUser(username, masterPassword): 
    hash = masterPasswordHash(masterPassword) 
    
    userData = {'UserName': username , 'MasterPassword': hash }
    fileName = 'data.json' 

    if os.exists(fileName): 
        with open(fileName , "a") as file: 
            json.dump(user_data, file)
            print("\nUser added\n")
    else: 
        with open(fileName , "x") as file: 
            json.dump(userData, file) 
            print("user added") 


