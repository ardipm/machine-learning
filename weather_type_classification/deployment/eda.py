import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title = 'Weather Type Dataset',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    st.title('Analysis of Weather Conditions Conducive to the sales of Cold allergy Medication')
    
    st.image('https://www.verywellhealth.com/thmb/hn77IdI0RBu6Z0CR9im0d1oVCD4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/hands-holding-pills-1271529649-09570fe280744fdda12d3cfd9ff42ea0.jpg',
             caption='Drugs | source: verywellhealth.com')
    
    st.write('__Weather Type Dataset__')

    # Show dataframe
    df = pd.read_csv('weather_classification_data.csv')
    st.dataframe(df,use_container_width=True)

    # Adjusting dataset
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(r'\s*\(.*\)\s*', '', regex=True)
    df.columns = df.columns.str.replace(' ', '_')

    df['is_snowy'] = df['weather_type'].apply(lambda x: 'Yes' if x == 'Snowy' else 'No')

    df_group_target = df.groupby('is_snowy').size().reset_index().rename(columns={0:'count'})

    labels = df_group_target['is_snowy']
    sizes = df_group_target['count']


    st.write('## Summary')
    st.markdown('''

    The target sale of cold allergy medications primarily in mountain and inland areas during the winter season. 
    The data shows that mountain areas experience the highest frequency of snowy weather, making them the prime target for selling medications for cold weather allergies, particularly those that alleviate breathlessness. 
    Inland areas also have a significant number of snowy days, indicating a strong market for these medications. 
    Coastal areas, with fewer snowy days, may still have occasional demand, especially during unexpected cold snaps. 
    Winter has the lowest average atmospheric pressure, often associated with colder weather and snowfall.
    This underscores the importance of having effective cold allergy medications available to address symptoms such as runny nose, cough, and shortness of breath, which often worsen during winter. 
    The imbalance in data distribution for snowy and not snowy areas could affect the accuracy of weather classification, potentially leading to misclassification.
    ''')
    
    st.markdown('---')

    # Plotting the pie chart
    with st.container():
        st.write('## Distribution of Snowy Days in Dataset')

        fig_1 = plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=65, colors=plt.cm.Set3.colors)
        plt.axis('equal')  
        st.pyplot(fig_1)
        st.write('The data in the dataset is imbalanced, as the percentage between snowy and non-snowy regions has a significant difference in the amount of data. ')

    st.markdown('---')
    
    st.markdown('## UV-Index Distribution by Season')
    st.markdown('__The intensity of ultraviolet radiation from the sun reaching the Earth\'s surface. High UV exposure can cause damage to human skin, such as sunburn, premature aging, and an increased risk of skin cancer.__')

    uv_index_avg = df.groupby('season')['uv_index'].mean().reset_index()

    st.dataframe(uv_index_avg, use_container_width=True)
    st.markdown('''
    Although winter sees lower average UV index levels, there remains a need for cold allergy medications that cater to symptoms exacerbated by cold weather. 
    Emphasizing formulations that soothe respiratory discomfort and nasal congestion can address specific winter-related allergic reactions.
    ''')

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

        # Plot for Spring
    axs[0, 0].hist(df[df['season'] == 'Spring']['uv_index'], bins=10, alpha=0.5, color='b')
    axs[0, 0].axvline(uv_index_avg[uv_index_avg['season'] == 'Spring']['uv_index'].values[0], color='r', linestyle='dashed', linewidth=1)
    axs[0, 0].set_title('Spring')
    axs[0, 0].set_xlabel('UV-Index')
    axs[0, 0].set_ylabel('Frequency')

        # Plot for Summer
    axs[0, 1].hist(df[df['season'] == 'Summer']['uv_index'], bins=10, alpha=0.5, color='g')
    axs[0, 1].axvline(uv_index_avg[uv_index_avg['season'] == 'Summer']['uv_index'].values[0], color='r', linestyle='dashed', linewidth=1)
    axs[0, 1].set_title('Summer')
    axs[0, 1].set_xlabel('UV-Index')
    axs[0, 1].set_ylabel('Frequency')

        # Plot for Autumn
    axs[1, 0].hist(df[df['season'] == 'Autumn']['uv_index'], bins=10, alpha=0.5, color='orange')
    axs[1, 0].axvline(uv_index_avg[uv_index_avg['season'] == 'Autumn']['uv_index'].values[0], color='r', linestyle='dashed', linewidth=1)
    axs[1, 0].set_title('Autumn')
    axs[1, 0].set_xlabel('UV-Index')
    axs[1, 0].set_ylabel('Frequency')

        # Plot for Winter
    axs[1, 1].hist(df[df['season'] == 'Winter']['uv_index'], bins=10, alpha=0.5, color='purple')
    axs[1, 1].axvline(uv_index_avg[uv_index_avg['season'] == 'Winter']['uv_index'].values[0], color='r', linestyle='dashed', linewidth=1)
    axs[1, 1].set_title('Winter')
    axs[1, 1].set_xlabel('UV-Index')
    axs[1, 1].set_ylabel('Frequency')

        # Adjust layout
    plt.tight_layout()
    st.pyplot(fig)
        
    st.markdown('''
    During the winter season, there is still has high levels of UV index, which means that UV levels can potentially become high at any time, posing risks to people's skin. 
    It's important for people to protect their skin by using sunscreen and limiting sun exposure during periods of high UV index, even in colder months when UV levels may not be as visibly intense as in summer.
    ''')

    st.markdown('---')

    st.markdown('## Atmospheric Pressure Distribution by Season')
    st.markdown('''
    __When atmospheric pressure drops, it often indicates the presence of colder or cloudier weather systems that can lead to snowfall. In areas with low atmospheric pressure, air tends to rise, cooling the atmosphere and forming clouds that can result in snow. 
    Therefore, monitoring atmospheric pressure can provide clues about the likelihood of snow in an area.__
    ''')

    ap_avg = df.groupby('season')['atmospheric_pressure'].mean().reset_index()
    st.dataframe(uv_index_avg, use_container_width=True)

    fig_2 = plt.figure(figsize=(8, 6))
    bars = plt.bar(ap_avg['season'], ap_avg['atmospheric_pressure'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.xlabel('Season')
    plt.ylabel('Atmospheric Pressure (hPa)')
    plt.title('Average Atmospheric Pressure by Season')
    plt.ylim(990, 1020) 

    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                round(bar.get_height(), 2), ha='center', va='bottom')

    st.pyplot(fig_2)

    st.markdown('''
    Winter season has lowest average of atmospheric pressure 999.65. 
    This low atmospheric pressure is often associated with colder weather and the possibility of snowfall. 
    This highlights the importance of availability of effective cold allergy medications to address symptoms such as runny nose, cough, and shortness of breath, which often worsen during winter.
    ''')

    st.markdown('---')
    st.markdown('## Number by Location')

    df_group_weather_type = df.groupby(['weather_type', 'location']).size().reset_index(name='count')

    fig_3 = plt.figure(figsize=(16, 8))
    sns.set(style = "whitegrid")
    sns.countplot(x = "weather_type", hue = "location", data = df, palette="colorblind")
    plt.ylabel('')
    plt.xlabel('Weather Type')
    plt.title('Distribution of Weather Types by Location')
    st.pyplot(fig_3)
    st.write('''
    
    __Mountain Regions__: With 1,605 number of snowy weather, mountain experience the highest frequency of snow. This makes them the prime target for selling medications for cold weather allergies, especially those that alleviate breathlessness.
    
    __Inland Regions__: Inland areas also have a significant number of snowy (1,575), indicating a strong market for these medications.
    
    __Coastal Regions__: Coastal areas have only 120 number of snowy weather. While the market is smaller, there may still be occasional demand, especially during unexpected cold snaps.
    
    ''')

    st.markdown('---')
    
    col1, col2 = st.columns(spec=[1,1], gap="large")

    with col1:
        
        st.write('### Humidity')
        st.markdown('''
        High humidity can exacerbate symptoms like nasal congestion and other respiratory conditions, while low humidity can cause throat irritation and dry nasal passages.
        ''')

        df_group_avg_humidity = df.groupby('location')['humidity'].mean().reset_index()

        fig_4 = plt.figure(figsize=(10, 6))
        plt.barh(df_group_avg_humidity['location'], df_group_avg_humidity['humidity'], color=['#FFB6C1', '#FFD700', '#87CEEB'])
        plt.xlabel('Humidity (%)')
        plt.title('Average Humidity Levels by Location')
        plt.xlim(0, 100)
        st.pyplot(fig_4)

        st.markdown('''
        
        For High Humidity Regions (Inland and Mountain): 

        - Develop and promote medications that address respiratory symptoms exacerbated by high humidity, such as congestion and shortness of breath.

        - consider offering combo packs that include both cold allergy medication and products that address humidity-related discomfort, like nasal sprays or humidifiers.

        For Lower Humidity Regions (Coastal): 

        - focus on medications that alleviate symptoms caused by dry air, such as dry skin.
        
        ''')
    with col2:
        
        st.write('### Temperature')
        st.markdown('''
        Cold temperatures can make symptoms of cold weather allergies like runny nose, coughing, and difficulty breathing worse for people who are sensitive to them.
        ''')


        df_group_avg_temp = df.groupby('location')['temperature'].mean().reset_index()

        fig_5 = plt.figure(figsize=(10, 6))
        sns.barplot(x='location', y='temperature', data=df_group_avg_temp, palette='viridis')
        plt.xlabel('Location')
        plt.ylabel('Temperature (Celsius)')
        plt.title('Average Temperature by Location')
        st.pyplot(fig_5)

        st.markdown('''
        Inland and Mountain areas experience lower temperatures compared to coastal regions. 
        Cold temperatures can exacerbate allergic reactions in susceptible individuals, leading to increased demand for cold allergy medications and related products.
        ''')
    st.markdown('---')

if __name__ == '__main__':
    run()