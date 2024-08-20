# Weather Classification: Snowy vs. Not Snowy

#### -- Project Status: Completed

### Methods Used
* Data Preprocessing
* Feature Engineering
* Random Forest Classification
* Cross-Validation
* Model Tuning and Evaluation
* Accuracy as a Metric

### Technologies
* Python
* Pandas
* Scikit-Learn
* Streamlit
* Hugging Face
* Matplotlib
* Seaborn

## Project Description

This project is focused on classifying weather conditions as either snowy or not snowy. The classification model developed will help forecast snowy conditions and manage the availability of cold allergy medications, particularly in regions prone to severe cold allergies. 

### Data Source:
The dataset used for this analysis is sourced from Kaggle's [Weather Classification Dataset](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma).

### Objectives:
1. **Develop a Classification Model:** Create a model to predict if the weather is snowy or not based on provided features.
2. **Achieve High Accuracy:** Aim for at least 90% accuracy in classifying weather conditions.
3. **Deploy the Model:** Implement the model using Streamlit and deploy it on Hugging Face for accessibility and usability.

### Analysis and Modeling Work:
1. **Exploratory Data Analysis (EDA):**
   - Analyzed weather patterns and identified key factors influencing snowy conditions.
   - Recommended targeted sales strategies for cold allergy medications based on weather data.

2. **Model Development:**
   - Used Random Forest Classification due to its effectiveness in handling imbalanced data and providing high accuracy.
   - Achieved a high accuracy of 97.08%, indicating a well-fitting model.
   - Conducted cross-validation and model tuning to refine performance.

3. **Insights and Recommendations:**
   - **Targeted Marketing:** Focus on mountain and inland areas during winter for cold allergy medication sales.
   - **Seasonal Strategies:** Emphasize medication distribution in winter due to lower atmospheric pressure and higher likelihood of snowfall.
   - **Product Development:** Develop medications for high humidity regions and consider product bundling for better customer satisfaction.

4. **Challenges:**
   - Addressing false negatives and false positives in the model to improve differentiation between cold and warm weather conditions.

## Getting Started

To reproduce or use this analysis, follow these steps:
1. **Clone the Repository:** `git clone https://github.com/your-repo/weather-classification-snowy.git`
2. **Install Dependencies:** Use `pip install -r requirements.txt` to install required Python packages.
3. **Data Setup:** Download the dataset from [Kaggle](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma) and place it in the appropriate directory.
4. **Run Analysis:** Execute the Jupyter notebook or Python script to perform data preprocessing, model training, and predictions.
5. **Deploy Model:** Use Streamlit to create a web app and deploy it on Hugging Face to make the model accessible for predictions.

## Contact

For any questions or further information, please contact:

- **Name:** [Ardiansyah Putra Mahadika]
- **Email:** [ardiansyahpm224@gmail.com]
- **LinkedIn:** [www.linkedin.com/in/ardiansyah-putra-m-17978318b]
