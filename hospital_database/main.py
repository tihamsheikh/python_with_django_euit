import os
import time
import datetime
from getpass import getpass

import user_pass_func
import database_func

prompt_global = """
What is your role
Press 1 for Manager
Press 2 for Doctor
enter 'q' to quit
>> 
"""

prompt_manager = """
Press 1 to 
Press 2 to 
Press 3 to 
enter '0' to go back
enter 'q' to quit
>>  
"""

# while action[0] == "q":
#     action = input(prompt).lower().strip()

# part 1 (login)
# take login info from a txt file like doctor or manager name and password 
# if the input matches the list of doctor or manager name then enter, after that prompt them password
# in the corresponding 

action = "1"

if action == "1":
    username = input("Username: ").strip()
    username_ls, password_ls = database_func.get_user_info("manager_list.csv")
    
    # prin  t(username_ls, password_ls)
    if username in username_ls:
        password = input("Password: ")
        if password in password_ls:
            print("logged in as manager")
        


# part 2 manager (taking serial)
# manager taking serial means to take paitent information (id, date, name, illness, ) and store them in a file
# also add a back button


# with open("paitent_info.txt") as f:
#     pass





