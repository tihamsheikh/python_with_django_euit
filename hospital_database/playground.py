import os
import hashlib
from csv import (reader, writer)
from datetime import datetime

def get_id(name: str)-> int:
    """
        used to convert paitent name into an id
    """
    hash_object = hashlib.md5(name.encode())  # encode string to bytes
    return int(hash_object.hexdigest(), 16) % (10 ** 8) # convert hex to integer (10** len of int)


base_dir = os.path.dirname(__file__)
user_list_path = os.path.join(base_dir, "database", "paitent_list.csv")
print(user_list_path)

name = "Tiham"
print(get_id(name))

with open(user_list_path, "a", newline="\n") as fp:
    file = writer(fp)
    
    # id, date, name, illness
    paitent_name = input("Paitent Name: ")
    illness = input("Paitent's Illness: ")

    file.writerow([get_id(paitent_name),datetime.now(),paitent_name,illness])
    print("Information is recorded")


def write_paitent_info(db_name: str):

    base_dir = os.path.dirname(__file__)
    user_list_path = os.path.join(base_dir, "database", db_name)
    print(user_list_path)

    with open(user_list_path, "a", newline="\n") as fp:
        file = writer(fp)
        
        paitent_name = input("Paitent Name: ")
        illness = input("Paitent's Illness: ")

        # id, date, name, illness
        file.writerow([get_id(paitent_name.lower().strip()),datetime.now(),paitent_name,illness])
    print("Information is recorded")