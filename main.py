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
    hashPass = hashlib.sha256()
    hashPass.update(password.encode())
    return hashPass.hexdigest()


#encryption key 
def makeKey():
    return Fernet.generate_key()

#creates a cipher with the key 
def initCipher(key): 
    return Fernet(key)

#encrypts passwords 
def encryptPassword(cipher, password): 
    return cipher.encrypt(password.encode()).decode()

#decrypt 
def decryptPassword(cipher, encryptedPassword):
    return cipher.decrypt(encryptedPassword.encode()).decode()

""" 
    Users and User data 
the functions that take care of user data 
"""

def newUser(userName, masterPassword): 
    hashPass = hashPassword(masterPassword) 
    key = makeKey().decode()

    userData = {'userName': userName , 'masterPassword': hashPass, 'key': key, 'passwords': []}
    fileName = 'data.json' 
    
    if os.path.exists(fileName): 
        with open(fileName , "r") as file: 
            try:
                data = json.load(file)
            except json.JSONDecodeError: 
                data = {}
        
        #adds the new user
        data[userName] = userData
        
        with open(fileName , "w") as file: 
            json.dump(data, file, indent=4) 
            print("\nUser added!\n") 

    else: 
        with open(fileName , "w") as file: 
            json.dump({userName: userData}, file, indent=4)
            print("user added") 

#add 
def addUserPass(userName, password, app, cipher): 

    try: 
        with open("data.json" , "r") as file: 
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        #error check for empty or broken json 
        data = {}

    #encrypt passwords 
    encryptedPassword = encryptPassword(cipher , password)

    #dictionary 
    item = {"app": app , "password": encryptedPassword }
    
    if userName not in data: 
        print("\nUser not found!\n")
        sys.exit()

    data[userName]["passwords"].append(item) 

    #save to file 
    with open("data.json" , "w") as file: 
        json.dump(data , file , indent=4) 

#login 
def login(userName, password):
    try: 
        with open("data.json") as file: 
            allUsers = json.load(file) 
        
        #error checking for user name 
        if userName not in allUsers: 
            print("not registered") 
            sys.exit()
        

        #check user entered password with master password
        userData = allUsers[userName]
        masterPasswordHash = userData.get("masterPassword")
        passwordAttemptHash = hashPassword(password)
        
        if passwordAttemptHash == masterPasswordHash and userName == userData.get("userName"):
            print("\nlogin successful")
            
            #global for the rest of the program 
            global cipher 
            # allows the cipher to be made and stored in the json 
            cipher = initCipher(userData["key"].encode())
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
            
            for entry in view[userName]["passwords"]: 
                decrypted = decryptPassword(cipher , entry["password"])
                print(f"{entry['app']}: {decrypted}")
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
                        app =input("APP:")
                        password = input("PASSWORD:")
                        addUserPass(userName , password , app, cipher)
                    case 2:            
                        #view all 
                        viewPasswords()
                    case 3: 
                        #return to menu 
                        break 
                    case _: 
                        print("invalid option!") 
                        



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



