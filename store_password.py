import bcrypt
import json
import os
import getpass
from check_password import check

username = input("Enter your username: ")

db_path = "./db.json"

if (not os.path.exists(db_path)):
    with open(db_path, "w") as f:
        json.dump({"users": []}, f)

with open(db_path, "r") as f:
    db = json.load(f)

user_exists = any(user["username"]==username for user in db["users"])

if (user_exists):
    next_step = input("User already exists. Do you want to update password? (Y/N): ")
    if (next_step not in ['Y', 'y']):
        print("Terminating session....")
        exit()

password = getpass.getpass(prompt="Enter password: ").encode()

hash = bcrypt.hashpw(password, bcrypt.gensalt()).decode()

if (user_exists):
    for user in db["users"]:
        if (user["username"]==username):
            if (check(password, user["password"])):
                print("Existing password entered.\nTerminating Session....")
                exit()
            user["password"] = hash
else:
    db["users"].append({
        "username": username,
        "password": hash
    })

with open(db_path, "w") as f:
    json.dump(db, f, indent=2)