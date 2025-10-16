from os import system
from time import sleep

def removing_repeatation(password: str)-> bool:
    dict = {}        
    for char in password:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    most_used_char = max([value for value in dict.values()])

    return most_used_char < len(password)-2 

def strong_pass_check(username: str)-> str:
    check: bool = True

    while check:
        system("clear")
        print(f"Password for this username '{username}'")
        password: str = input("Choose a password: ") 
        if password.isdigit() or password.isalpha() or len(password) < 10 or password.isalnum():
            review = "password too short" if len(password) < 10 else "use different character"  
            print(review)
            sleep(.5)
            system("clear")
            continue

        if not password.isalnum() and removing_repeatation(password):
            print("Account created")
            check = False
            break

    return password

def encou_rage_ment():
    system("clear")
    print("Good job, you logged in!")
    sleep(3)
    print("but for what ^_^")
    sleep(3)
    print("BYE!!")
    sleep(3)
    system("clear")
