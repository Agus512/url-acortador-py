import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

#Creacion de web con streamlit
st.set_page_config(page_title="URL Shortener",page_icon="🧠", layout="centered")
st.image("code512.png", use_column_width=True)
st.title("URL Shortener")
url = st.text_input("Enter the URL")
if st.button("Generate new URL"):
    st.write("URL shortened: ", shorten_url(url))
#PARA INICIALIZAR SE DEBE USAR ( python -m streamlit run (nombre del archivo.py))
# python -m streamlit run url_shortener.py
