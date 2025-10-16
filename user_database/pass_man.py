# make a strong password checker
# make a username & password checker and if password is not strong return again to enter new password
# store password in a dict and if user in dict log them in if not quit
# make option login, create new user, rename password, rename username
# EXTRA 
# use a class database if not bored
# test case &&&&&&&&?

from os import system
from time import sleep
from pass_mans_func import *

system("clear")

dict: dict = {}
action: str = ""
prompt = """
>Press 1 to login in
>Press 2 to create a new account
>Press 3 to delete username
>Press 4 to update username
>Press 5 to update password
>Type 'q' to quit (beta 0.1)
"""

while action != "q":
    system("clear")

    # print(dict)
    print(prompt, end="\n")
    action = input(">>> ").lower().strip()

    if action == "1":
        username: str = input("Your username: ").strip()
        if username in dict.keys():
            password: str = input("Your password: ")
            if password in dict.values():
                encou_rage_ment()
        
            else:
                print("Password did not match, GFY!!")
        else:
            print("Oops didn't match the username dawg!")
            print("Try again or something like that")
            sleep(2.5)
            continue
        
    elif action == "2":

        username: str = input("Make a username: ").strip()
        
        if username not in dict.keys():
            password = strong_pass_check(username)
            dict[username] = password
            sleep(1.5)
            system("clear")

        else:
            print("Username already extists!")
            sleep(1.5)
            system("clear")
            continue    
        
    elif action == "3":
        username: str = input("Make a username: ").strip()

        if username in dict.keys():
            del dict[username]
        else:
            print("Username does not exists!")


