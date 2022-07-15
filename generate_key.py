import pickle
from pathlib import Path
import streamlit_authenticator as stauth
from mysqlDB import connectToDB


def generatePassword():
    mydb, mycursor = connectToDB()

    mycursor.execute("SELECT username,email,password FROM users")
    myresult = mycursor.fetchall()

    usernames = []
    emails = []
    passwords = []

    for x in myresult:
        usernames.append(x[0])
        emails.append(x[1])
        passwords.append(x[2])

    hashed_passwords = stauth.Hasher(passwords).generate()

    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("wb") as file:
        pickle.dump(hashed_passwords, file)

    return usernames,emails,hashed_passwords
