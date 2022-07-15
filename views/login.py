import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth
from mysqlDB import connectToDB
from generate_key import generatePassword

from views import home


def authLogOut():
    usernames, emails, hashed_passwords = generatePassword()

    #LOAD hashed Passwords
    file_path = Path(
        __file__).parent / "G:\\MyCodeprojects\\Minor Project\\streamlit music recommendation\\hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    authenticator = stauth.Authenticate(usernames, emails, hashed_passwords,
                                        "music_dashboard", "abcdef", cookie_expiry_days=30)

    # default login page and also pass where it locate in main or sidebar
    name, authentication_status, username = authenticator.login("Login", "main")

    return name, authentication_status, username,authenticator



def load_view():
    name, authentication_status, username,authenticator = authLogOut()

    if authentication_status == False:
        st.error("Username/password is incorrect")
    elif authentication_status == None:
        st.warning("Please enter your username and password")
    elif authentication_status:
        #authenticator.logout("Logout", "main")         #sidebar
        #home.load_view(authenticator,name)
        from views import userhomepage
        userhomepage.load_view(authenticator,name,username)


