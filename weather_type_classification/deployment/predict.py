import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

with open('./deployment/model_rf.pkl', 'rb') as file_1:
  model = pickle.load(file_1)
  
def run():
    st.markdown("<h1 style='text-align: center;'>Classify Model (Weather Type)</h1>", unsafe_allow_html=True)
    # st.write("# Classify Model (Weather Type)")
    
        
    with st.form("my_form"):
        season = st.selectbox('Season', ['Winter', 'Spring', 'Summer', 'Autumn'], index=1)
        location = st.radio('Location ', ['Inland', 'Mountain', 'Coastal'], index=1)
        cloud_cover = st.selectbox('Cloud cover', ['Clear', 'Overcast', 'Partly Cloudy', 'Cloudy'], index=0)
        with st.container():
            visibility = st.number_input('Visibility (in Km)', value=0, max_value=35)
            
        col1, col2 = st.columns(spec=[1,1], gap="large")
        
        with col1:
            temperature = st.number_input('Temperature (Celcius)', value=28, min_value=-10, max_value=45)
            humidity = st.slider('Humidity', min_value=15, max_value= 110)
            precipitation = st.number_input('Precipitation', value=0, max_value=110)

        with col2:
            wind_speed = st.number_input('Wind Speed', value=0, max_value=110)
            uv_index = st.slider('UV - Index', min_value=0, max_value=15)
            atmospheric_pressure = st.number_input('Atmospheric Pressure', max_value=1300)
        
        submitted = st.form_submit_button("Submit", use_container_width=True)
        
    sample_data = {
    'temperature': temperature, 
    'humidity': humidity, 
    'wind_speed': wind_speed, 
    'precipitation': precipitation, 
    'cloud_cover': cloud_cover,
    'atmospheric_pressure': atmospheric_pressure, 
    'uv_index': uv_index, 
    'season': season, 
    'visibility': visibility, 
    'location': location
    }

    data_inf = pd.DataFrame([sample_data])

    if submitted:
        with st.container():
            progress_text = "Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(0.005)
            my_bar.empty()
            
            st.dataframe(data_inf, use_container_width=True)
    
            result= model.predict(data_inf)
            if result[0] == 0:
                st.markdown("<h3 style='text-align: center;'>It's Not Snowy!</h3>", unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown("<h3 style='text-align: center;'>It's Snowy!</h3>", unsafe_allow_html=True)
                st.snow()
                 
if __name__ == '__main__':
    run()