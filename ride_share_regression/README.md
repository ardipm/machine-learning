# Ride-Hailing Price Prediction

#### -- Project Status: Completed

### Methods Used
* Linear Regression
* Data Preprocessing and Feature Engineering
* Exploratory Data Analysis (EDA)
* Model Evaluation Metrics (e.g., MAE, R-squared)

### Technologies
* Python
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn
* Jupyter Notebook

## Project Description

This project aims to analyze and predict ride-hailing trip fares from two major companies, Uber and Lyft. The goal is to build a predictive model that can forecast future trip costs and evaluate which service offers more economical pricing.

### Data Source:
The dataset used for this analysis is sourced from Kaggle: [Uber and Lyft Dataset - Boston, MA](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma). This dataset includes ride-hailing trip data from Uber and Lyft in Boston.

### Objectives:
1. **Develop a Predictive Model:** Create a model to forecast trip fares for Uber and Lyft.
2. **Compare Pricing:** Assess which ride-hailing service provides more cost-effective pricing.
3. **Forecast Future Costs:** Utilize the model to predict fares for upcoming trips.

### Analysis and Modeling Work:
1. **Exploratory Data Analysis (EDA):**
   - Analyzed fare distribution and ride counts across different areas.
   - Identified popular areas and peak times affecting ride demand.

2. **Model Development:**
   - Implemented a linear regression model to predict trip fares.
   - Evaluated model performance using Mean Absolute Error (MAE) and R-squared metrics.
   - Achieved an MAE of approximately $1.82 and an R-squared score of 0.92, indicating high accuracy in fare predictions.

3. **Insights:**
   - Uber has a larger user base compared to Lyft, indicating stronger consumer preference.
   - Price distribution ranges around $20, consistent with standard fare structures.
   - High ride counts observed in areas like the Financial District and Theatre District.
   - Increased demand during rush hours, affecting operational strategies.

### Challenges:
- Ensuring data quality and consistency across different sources.
- Refining the model to handle variations in fare predictions and optimize performance.

## Getting Started

To reproduce this analysis, follow these steps:
1. **Clone the Repository:** `git clone https://github.com/your-repo/ride-hailing-price-prediction.git`
2. **Install Dependencies:** Use `pip install -r requirements.txt` to install the required Python packages.
3. **Data Setup:** Download the dataset from [Kaggle](https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma) and ensure it is placed in the appropriate directory.
4. **Run Analysis:** Execute the Jupyter notebook or Python script to perform data analysis, model training, and predictions.
5. **Review Results:** Examine the predictions, insights, and model performance metrics.

## Contact

For any questions or further information, please contact:

- **Name:** [Ardiansyah Putra Mahadika]
- **Email:** [ardiansyahpm224@gmail.com]
- **LinkedIn:** [www.linkedin.com/in/ardiansyah-putra-m-17978318b]
