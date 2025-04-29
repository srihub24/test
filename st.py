import streamlit as st
import pandas as pd
st.title("Streamlit File")
st.write('hello')
f=st.file_uploader("Upload your files here")
res=pd.read_csv(f)
res1=res.to_csv("res1.csv")
st.download_button("Download",data=res,file_name="res1.csv")
