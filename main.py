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
def hashPassword(password): 
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
    encryptedPassword = encryptPassword(cipher)

#add 
def addUserPass(password, site): 

    try: 
        with open("data.json" , "w") as file: 
            data = json.load(file)
    except json.JSONDecodeError:
        #error check for empty or broken json 
        data = [] 

    #encrypt passwords 

#login 
def login(userName, password):
    try: 
        with open("data.json") as file: 
            userData = json.load(file) 
        
        #check user entered password with master password
        masterPasswordHash = userData.get("masterPassword")
        passwordAttemptHash = hashPassword(passwordAttemptHash)
        
        if passwordAttemptHash == masterPasswordHash and userName == userData.get("userName"):
            print("\nlogin successful")
        else: 
            print("\nlogin unsuccessful")
            #exit
            sys.exit()
    except Exception: 
        print("\nYoure not registered") 
        #exit
        sys.exit()

#view passwords
def viewPasswords(): 
    try: 
        with open("data.json", "r") as data:
            view = json.load(data)
            print("\nyour passwords")

            for password in view: 
                print(x["website"])
            print("\n")
    except FileNotFoundError: 
        print("\nYou havent saved any passwords")





