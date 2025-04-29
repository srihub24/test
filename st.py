import streamlit as st
st.title("Streamlit File")
st.write('hello')
f=st.file_uploader("Upload your files here")
st.download_button('Download The File',f)
