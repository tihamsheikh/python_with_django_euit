import os
from csv import reader


def get_user_info(db: str)-> tuple:
    """
        gets the username and password from a csv file -> (list, list)
    """
    base_dir = os.path.dirname(__file__)
    user_list_path = os.path.join(base_dir, "database", db)

    with open(user_list_path) as fp:
        username, password = [], []
        info = reader(fp)
        next(info)

        for i in info:
            username.append(i[0])
            password.append(i[1])
    return username, password



