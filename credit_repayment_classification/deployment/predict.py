import streamlit as st
import pandas as pd
import numpy as np
import pickle
with open('model_log.pkl', 'rb') as file_1:
  model = pickle.load(file_1)

def run():
    st.write("# Predictive Model (Credit Card User Repayment)")

    
    with st.form("my_form"):
        limit_amount = st.number_input('Input your balance limit', min_value= 10000, value=10000)
        age = st.number_input('Input your age', min_value=20, value=20)
        gender = st.radio('Gender', ['Male','Female'], index=1)
        marital_status = st.radio('Marital Status', ['Married','Single','Other'], index=1)
        education_level = st.radio('Education Level', ['University', 'High School', 'Graduate School', 'Unkown', 'Others'], index=1)
        
        pay_0 = st.selectbox('Your payment status this month', [
                                                'No Transaction', 
                                                'Pay Duly',
                                                'No Late Payment', 
                                                'payment delay for one month', 
                                                'payment delay for two months',
                                                'payment delay for three months',
                                                'payment delay for four months',
                                                'payment delay for five months',
                                                'payment delay for six months', 
                                                'payment delay for seven months', 
                                                'payment delay for eight months', 
                                                'payment delay for nine months and above', 
                                                ], index=0, placeholder="Choose an option")
        pay_2 = st.selectbox('Your payment status last month', [
                                                'No Transaction', 
                                                'Pay Duly',
                                                'No Late Payment', 
                                                'payment delay for one month', 
                                                'payment delay for two months',
                                                'payment delay for three months',
                                                'payment delay for four months',
                                                'payment delay for five months',
                                                'payment delay for six months', 
                                                'payment delay for seven months', 
                                                'payment delay for eight months', 
                                                'payment delay for nine months and above', 
                                                ], index=0, placeholder="Choose an option")
        pay_3 = st.selectbox('Your payment status last 3 months', [
                                                'No Transaction', 
                                                'Pay Duly',
                                                'No Late Payment', 
                                                'payment delay for one month', 
                                                'payment delay for two months',
                                                'payment delay for three months',
                                                'payment delay for four months',
                                                'payment delay for five months',
                                                'payment delay for six months', 
                                                'payment delay for seven months', 
                                                'payment delay for eight months', 
                                                'payment delay for nine months and above', 
                                                ], index=0, placeholder="Choose an option")
        pay_4 = st.selectbox('Your payment status last 4 months', [
                                                'No Transaction', 
                                                'Pay Duly',
                                                'No Late Payment', 
                                                'payment delay for one month', 
                                                'payment delay for two months',
                                                'payment delay for three months',
                                                'payment delay for four months',
                                                'payment delay for five months',
                                                'payment delay for six months', 
                                                'payment delay for seven months', 
                                                'payment delay for eight months', 
                                                'payment delay for nine months and above', 
                                                ], index=0, placeholder="Choose an option")
        pay_5 = st.selectbox('Your payment status last 5 months', [
                                                'No Transaction', 
                                                'Pay Duly',
                                                'No Late Payment', 
                                                'payment delay for one month', 
                                                'payment delay for two months',
                                                'payment delay for three months',
                                                'payment delay for four months',
                                                'payment delay for five months',
                                                'payment delay for six months', 
                                                'payment delay for seven months', 
                                                'payment delay for eight months', 
                                                'payment delay for nine months and above', 
                                                ], index=0, placeholder="Choose an option")
        pay_6 = st.selectbox('Your payment status last 6 months', [
                                                'No Transaction', 
                                                'Pay Duly',
                                                'No Late Payment', 
                                                'payment delay for one month', 
                                                'payment delay for two months',
                                                'payment delay for three months',
                                                'payment delay for four months',
                                                'payment delay for five months',
                                                'payment delay for six months', 
                                                'payment delay for seven months', 
                                                'payment delay for eight months', 
                                                'payment delay for nine months and above', 
                                                ], index=0, placeholder="Choose an option")
        
        bill_amount_1 = st.slider('Input your latest bill amount', min_value= 10000, value=10000000)
        bill_amount_2 = st.slider('Input your last month bill amount', min_value= 10000, value=10000000)
        bill_amount_3 = st.slider('Input your last 2 months bill amount', min_value= 10000, value=10000000)
        bill_amount_4 = st.slider('Input your last 3 months bill amount', min_value= 10000, value=10000000)
        bill_amount_5 = st.slider('Input your last 4 months bill amount', min_value= 10000, value=10000000)
        bill_amount_6 = st.slider('Input your last 5 months bill amount', min_value= 10000, value=10000000)
        
        pay_amount_1 = st.number_input('Input amount of your previous payment in September 2005', min_value= 10000, value=1000000)
        pay_amount_2 = st.number_input('Input amount of your previous payment in August 2005', min_value= 10000, value=1000000)
        pay_amount_3 = st.number_input('Input amount of your previous payment in July 2005', min_value= 10000, value=1000000)
        pay_amount_4 = st.number_input('Input amount of your previous payment in June 2005', min_value= 10000, value=1000000)
        pay_amount_5 = st.number_input('Input amount of your previous payment in May 2005', min_value= 10000, value=1000000)
        pay_amount_6 = st.number_input('Input amount of your previous payment in April 2005 ', min_value= 10000, value=1000000)
        
        # # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")

    data_inf = {
        'limit_balance': limit_amount,
        'sex': gender,
        'education_level': education_level,
        'marital_status': marital_status,
        'age': age,
        'pay_0':pay_0, 
        'pay_2':pay_2, 
        'pay_3':pay_3, 
        'pay_4':pay_4, 
        'pay_5':pay_5, 
        'pay_6':pay_6,
        'bill_amt_1':bill_amount_1,
        'bill_amt_2':bill_amount_2, 
        'bill_amt_3':bill_amount_3, 
        'bill_amt_4':bill_amount_4, 
        'bill_amt_5':bill_amount_5, 
        'bill_amt_6':bill_amount_6,
        'pay_amt_1':pay_amount_1, 
        'pay_amt_2':pay_amount_2, 
        'pay_amt_3':pay_amount_3, 
        'pay_amt_4':pay_amount_4, 
        'pay_amt_5':pay_amount_5,
        'pay_amt_6':pay_amount_6
    }

    data_inf = pd.DataFrame([data_inf])

    st.dataframe(data_inf)
        

    if submitted:
        result= model.predict(data_inf)
        if result[0] == 0:
            st.write(f'## Default Status: Not Default')
        else:
            st.write(f'## Default Status: Default')
        
if __name__ == '__main__':
    run()