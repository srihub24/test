import pandas as pd
import streamlit as st
st.title("Anomaly detection")
uploaded_file=st.file_uploader("Upload your file here")
if uploaded_file:
  df=pd.read_csv(uploaded_file)
  st.write(df.describe())
