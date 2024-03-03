import LoginUser as lu
import sqlite3

conn = sqlite3.connect('./passwords.sqlite')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users (
        name TEXT,
        lastname TEXT,
        phone TEXT,
        email TEXT PRIMARY KEY,
        password TEXT
    )
""")
conn.commit()
conn.close()

correctPassword = lu.password

databasepasswords = []

def addpasswords ():
    databasepasswords.append(correctPassword)
    print(databasepasswords)

def checkpassword (n):
    n.map(addpasswords)

    if correctPassword == a:
        print("Password is correct")
    else:
        print("Password is incorrect")