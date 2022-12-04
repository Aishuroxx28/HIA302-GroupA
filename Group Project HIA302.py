#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load cases_malaysia CSV file using Pandas
#use head function to view the first 5 dataset values

import pandas as pd
df = pd.read_csv(r'C:\Users\Acer\Desktop\group_project302\cases_malaysia.csv')
print(df.head())


# In[2]:


#select columns called 'date' and 'cases_new'
#drop certain rows based on date column with row value less than 2022-08-01. Value needed is from 2022-08-01 until 2022-11-30

df= df[['date', 'cases_new']]
df= df.drop(df[df['date']<'2022-08-01'].index)
df =df.drop(df[df['date']>'2022-11-30'].index)
print(df)


# In[3]:


#to review the shape and size of the dataframe.
print(df.shape)


# In[4]:


#to list the data types used by by the dataframe to characterize each attribute. 
print(df.dtypes)


# In[5]:


#to show the descriptive analysis of the dataframe
print(df.describe())


# In[6]:


#to check for missing values in each columns

missing_data = df.isnull().mean()*100
missing_data.sort_values(ascending=False)


# In[21]:


#import required modules
import altair as alt

alt.Chart(df).mark_bar().encode(
    x = "date",
    y = "cases_new",
    #tooltip is to display x and y variables associated "date" and "cases_new" respectively
    tooltip=['date','cases_new'],
    #The highlight is set based on the result of the conditional statement
    color=alt.condition(
        #select and highlight 'red' the dates selected due to public holidays
        alt.FieldOneOfPredicate ('date', ['2022-08-01', '2022-08-31', '2022-09-16', '2022-09-09', '2022-09-10', '2022-10-24', '2022-11-04', '2022-11-11', '2022-11-12', '2022-11-19', '2022-11-20', '2022-11-29']),
        alt.value('red'), 
        # the color is set to 'steelblue' for the dates that do not satisfy the condition .
        alt.value('steelblue') 
    )  
).properties(width=1000)

