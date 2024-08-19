import streamlit as st
import eda
import predict

navigation = st.sidebar.selectbox('Choose page:', ['EDA', 'Predict'])

if navigation == 'EDA':
    eda.run()
else:
    predict.run()