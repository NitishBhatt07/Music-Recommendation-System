import streamlit as st
import base64
#
# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()
#
#
# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://cdn.wallpapersafari.com/48/11/uRFcp7.jpeg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

def load_view():
    set_bg_hack_url()
    st.title("Yooo")
    # set_png_as_page_bg('background.png')
