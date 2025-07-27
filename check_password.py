import bcrypt

def check(password, stored_hash):
    if (type(password)==str):
        password = password.encode()
    if (type(stored_hash)==str):
        stored_hash = stored_hash.encode()
    try:
        return bcrypt.checkpw(password, stored_hash)
    except Exception as e:
        print("Invalid hash or password:", e)
        return False
