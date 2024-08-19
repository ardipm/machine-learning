import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title = 'Credit Card Dataset',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    st.title('Credit Payment Analysis')
    
    # menambahkan gambar
    st.image('https://time.com/personal-finance/static/84016af8afe9681354d097200e07945e/ca7ff/credit-card-types.jpg',
             caption='visa credit card | source: time.com')
    
    st.write('# Credit Card Dataset')
    
    # Show dataframe
    df = pd.read_csv('P1G5_Set_1_ardiansyah_putra.csv')
    st.dataframe(df)
    
    st.write('## The average latest bill of customers who have overdue (in month) status on credit card payments.')
    
    # Creating new table that provides the average bill amount for customers grouped by their default payment status for the next month.
    df_group_1 = df.loc[(df['pay_0'] > 0)].groupby('default_payment_next_month')['bill_amt_1'].mean().reset_index()
    df_group_1
    
    fig_1 =plt.figure(figsize=(10, 6))
    sns.barplot(x='default_payment_next_month', y='bill_amt_1', data=df_group_1)
    plt.xlabel('Default Payment Next Month')
    plt.ylabel('Averge Bill Amount in September 2005 (NT dollars)')
    plt.title('Average Bill Amount in September 2005 by Default Payment Status')
    st.pyplot(fig_1)
    
    st.write(
        '''
        The average credit card bill for customers who still have outstanding payments and are marked as default in their repayment next month is about 56,875. 
        High average bill amount for customer who as default status on next month repayment suggests that these customers represent a substantial risk to the bank in terms of potential losses
        ''')
    
    st.markdown('---')
    
    st.write('## Characteristic of limit balance of credit card user ')

    avg_limit_balance = df['limit_balance'].mean()

    
    
    # Grouping new category based on above average of limit balance
    df_group_2 = df.loc[df['limit_balance'] > avg_limit_balance].groupby('default_payment_next_month').size().reset_index().rename(columns={0:'count'})
    df_group_2
    # Grouping new category based on less than average of limit balance
    df_group_3 = df.loc[df['limit_balance'] < avg_limit_balance].groupby('default_payment_next_month').size().reset_index().rename(columns={0:'count'})
    df_group_3
    
    fig_3, axs = plt.subplots(1, 2, figsize=(16, 8))

    # First pie chart for customers with credit limit below average
    axs[0].pie(df_group_3['count'], labels=df_group_3['default_payment_next_month'].map({0: 'Not Default', 1:'Default'}), autopct='%1.1f%%', startangle=140)
    axs[0].set_title('Limit Balance Below Average by Default Payment Status')
    axs[0].axis('equal')

    # Second pie chart for customers with credit limit above average
    axs[1].pie(df_group_2['count'], labels=df_group_2['default_payment_next_month'].map({0: 'Not Default', 1: 'Default'}), autopct='%1.1f%%', startangle=140)
    axs[1].set_title('Limit Balance Above Average by Default Payment Status')
    axs[1].axis('equal')
    st.pyplot(fig_3)
    
    st.write('''
             Customers with higher limit balance are less likely to default on their payments compared to those with lower credit limits.
             Customers with lower credit limits might need more monitoring and proactive measures to reduce the risk of default, such as early warnings or financial advice.
             For customers with higher credit limits, although the default rate is lower, it is still important to monitor their payment behavior as they constitute a significant portion of the bank’s credit exposure.
             ''')
    
    st.write('## Average of limit balance credit card users')
    
    fig_2 = plt.figure(figsize=(10, 6))
    sns.histplot(df['limit_balance'], bins=30, kde=True)
    plt.axvline(avg_limit_balance, color='r', linestyle='dashed', linewidth=1)
    plt.xlabel('Limit Balance (NT dollars)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customer Limit Balance')
    plt.legend({'Average Limit Balance': avg_limit_balance})
    st.pyplot(fig_2)
    st.markdown('---')
    
    
    st.write('## Characteristic of limit balance of credit card user ')
    # Calculating average of users' age
    avg_age = df['age'].mean()
        
    fig_4 = plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=30, kde=True)
    plt.axvline(avg_age, color='r', linestyle='dashed', linewidth=1)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customers\' Age')
    plt.legend({'Average Age of Credit Card Users': avg_age})
    st.pyplot(fig_4)
    
    
    st.write('Age distribution of credit card users with default payment status next month')
    # Determine age range 
    bins = [20, 30, 40, 50, 60, 70]
    labels = ['20-29', '30-39', '40-49', '50-59', '60-69']
    
    # Create a new column 'age_category' in order to analyzing based on age range
    df['age_category'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    df_group_age = df.loc[df['default_payment_next_month'] == 1].groupby('age_category').size().reset_index(name='count')
    df_group_age
    
    
    fig_5 = plt.figure(figsize=(10, 8))
    sns.barplot(x='count', y='age_category', data=df_group_age.sort_values(by='count',ascending=False), orient='h')
    plt.title('Distribution of Default Payment Next Month by Age Category')
    st.pyplot(fig_5)
    
    st.write('''
             The younger credit card users (in range 20-29 and 30-39) are more likely to default on their payments compared to older age groups. 
             There is a clear decreasing trend in the number of defaulters as age increases. The number of marked as default significantly drops in the age groups 40-49 (140), 50-59 (51), and 60-69 (9).
             ''')
    st.markdown('---')
    # diplay count of credit card user with their default status payment next month
    default_counts = df['default_payment_next_month'].value_counts().reset_index()
    
    default_counts.columns = ['default_payment_next_month', 'count']
    
    # Create a horizontal bar plot
    st.write('''
             ## Total number of Credit Card User
             ''')
    st.write('''
             There are 635 credit card users with a default payment status next month in Total.
             ''')
    fig_6 = plt.figure(figsize=(10, 6))
    sns.barplot(x='count', y='default_payment_next_month', data=default_counts, orient='h')
    plt.xlabel('Count')
    plt.ylabel('Default Payment Next Month')
    plt.title('Count of Default Payment Status for Next Month')
    st.pyplot(fig_6)

    st.write('''
            ### Categorized by Gender         
            ''')
    
    # Creating new table (dataframe) that provides count of customer's gender grouped by their default payment status for the next month.
    df_group_4 = df.loc[df['default_payment_next_month'] == 1].groupby('sex').size().reset_index().rename(columns={0:'count'})
    df_group_4
    
    fig_6 =plt.figure(figsize=(8, 8))
    plt.pie(df_group_4['count'], labels=df_group_4['sex'].map({1: 'Male', 2: 'Female'}), autopct='%1.1f%%', startangle=140)
    plt.title('Default Payment Next Month by Gender')
    plt.axis('equal')
    st.pyplot(fig_6)

    st.write('''
             Female customers have a higher tendency to default on their credit card payments compared to male customers in this dataset.
             The higher default rate among female customers could be influenced by various factors such as income levels, spending behavior, or access to financial management literature.             
             ''')
    
if __name__ == '__main__':
    run()