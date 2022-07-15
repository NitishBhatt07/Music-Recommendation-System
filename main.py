import streamlit as st
import utils as utl
from views import register,login,options,configuration,home,default

st.set_page_config(layout="wide", page_title='Music Recommendation System')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "register":
        register.load_view()
    elif route == "login":
        login.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()