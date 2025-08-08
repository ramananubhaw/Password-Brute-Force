import os
import json
from check_password import check

username = input("Enter username: ")

db_path = "./db.json"

if (not os.path.exists(db_path)):
    print("Invalid username")
    exit()

with open(db_path, 'r') as f:
    db = json.load(f)

found = False
for user in db["users"]:
    if (user["username"]==username):
        found = True
        hash = user["password"]
        break

if (not found):
    print("Invalid username")
    exit()

# print(hash)

chars = []

for i in range(26):
    chars.append(chr(ord('a')+i))
    chars.append(chr(ord('A')+i))

for i in range(10):
    chars.append(chr(ord('0')+i))

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '_', '=', '<', '>', '?', '~', '[', ']', '{', '}', '/', '|']

for c in special_chars:
    chars.append(c)

# chars.reverse()

# print(chars)

queue = chars.copy()

cracked = False
while (queue):
    guess = queue.pop(0)
    print(guess)
    if (check(guess, hash)):
        cracked = True
        break
    for c in chars:
        queue.append(guess+c)

if (cracked):
    print(f"Password cracked: {guess}")
else:
    print("Password could not be cracked.")