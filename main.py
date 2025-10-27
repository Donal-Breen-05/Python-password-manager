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
def addUserPass(password, app): 

    try: 
        with open("data.json" , "w") as file: 
            data = json.load(file)
    except json.JSONDecodeError:
        #error check for empty or broken json 
        data = [] 

    #encrypt passwords 
    encryptedPassword = encryptPassword(cipher , password)

    #dictionary 
    item = {"app": app , "password": encryptedPassword }
    data.append(item) 
    
    #save to file 
    with open("data.json" , "w") as file: 
        json.dump(data , file , indent=4) 

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

"""
    MAIN loop 
"""
while True: 
    
    #gui 
    print("\tPassword manager\n") 
    print("-------------------")
    print("(1) login")
    print("(2) register")
    print("(3) exit")

    #choice
    option = int(input("choose option: "))
    match option: 
        case 1: 
            #login user 
            print("\nEnter your User Name and password: ")
            userName = input("USERNAME: ")
            masterPassword = input("PASSWORD: ")
            login(userName, masterPassword)
            

            #ADD PASSWORDS LOOP  
            while True: 
                 
                # add or view passwords 
                print("(1) add ") 
                print("(2) view password")
                print("(3) view all") 
                print("(4) return to Menu") 
            
                option2 = int(input("choose option:"))
            
                match option2: 
                    case 1: 
                        #add password
                        addUserPass()
                    case 2: 
                        #view specific password 
                        viewPasswords()
                    case 3: 
                        #view all 
                        viewPasswords()
                    case 4: 
                        #return to menu 
                        break 
                    case _: 
                        print("invalid option!") 
                        #TODO: finish the add/remove passwords code 



        case 2: 
            #register user  
            print("\nEnter your User Name and password: ")
            userName = input("USERNAME: ")
            masterPassword = input("PASSWORD: ")
            newUser(userName, masterPassword) 
        case 3: 
            #exit
            print("\nGoodbye!") 
            sys.exit()
        #default 
        case _: 
            print("invalid input! ") 



