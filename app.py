import pandas as pd
import streamlit as st
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
st.title("Anomaly detection")
uploaded_file=st.file_uploader("Upload your file here")
if uploaded_file:
  df=pd.read_csv(uploaded_file)
  st.write(df.describe())
  features = ['TransactionAmount', 'TransactionDuration', 'AccountBalance', 'LoginAttempts']  # Modify as needed
  X = df[features].copy()
  X = X.fillna(X.mean())
# Standardize the features 
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)
  st.write(X_scaled)
  iso_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
  iso_forest.fit(X_scaled)

# Predict anomalies
  df['AnomalyScore'] = iso_forest.decision_function(X_scaled)
  df['IsAnomaly'] = iso_forest.predict(X_scaled)
  st.write("Fraud tranactions")
  st.write(df[df['IsAnomaly']==-1])
  st.write("Number of Fraud transactions")
  st.write((df['IsAnomaly']==-1).sum())
