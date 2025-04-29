import streamlit as st
import pandas as pd
st.title("Streamlit File")
st.write('hello')
f=st.file_uploader("Upload your files here")
res=pd.read_csv(f)
res1=f.to_csv().encode("utf-8")
st.download_button("Download",res1)
