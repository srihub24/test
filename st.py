import streamlit as st
st.title("Streamlit File")
st.write('hello')
st.file_uploader("Upload your files here")
a=st.text_input("Enter a")
st.write(a)
