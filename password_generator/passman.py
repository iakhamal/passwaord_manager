import hashlib
import getpass

#managing passwords 

password_manager ={}
def get_account():
    username = input ("create your username: ")
    password = getpass.getpass("enter your passwod: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username]= hashed_password
    print ("account created")

def login():
    username = input("enter your username: ")
    password =getpass.getpass("enter your passweord")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username]==hashed_password:
        print("login successfully ")
    else: 
        print ("invalid credential")

def main():
    while True:
        choice = input("enter 1 to create an account , 2 to login, or 0 to exit: ")
        if choice=="1":
            get_account()
        elif choice=="2":
            login()
        elif choice=="0":
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()