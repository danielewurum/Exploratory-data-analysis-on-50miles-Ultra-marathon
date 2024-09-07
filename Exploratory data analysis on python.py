#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install seaborn')


# In[5]:


import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup


# In[9]:


#import data into jupyter notebook
df = pd.read_csv(r"C:\Users\DAN\Downloads\for py\data.csv")


# In[11]:


df


# In[13]:


#we use the isin function to combine both 50km and 50mi
df[df['Event distance/length'].isin(['50km', '50mi'])]


# In[87]:


df.shape


# In[88]:


df.dtypes


# In[12]:


#Let's do some data cleaning since we only need event with 50km and 50 miles

df[df['Event distance/length'] == '50km']


# In[17]:


# We need to limit the year of event to 2020 only

df[(df['Event distance/length'].isin(['50km', '50mi'])) & (df['Year of event'] == 2020)]


# In[18]:


#Let's filter the events to only the races that too place in the USA


# In[25]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']


# In[29]:


df[(df['Event distance/length'].isin(['50km', '50mi']))
   & (df['Year of event'] == 2020)
   & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[30]:


df2 = df[(df['Event distance/length'].isin(['50km', '50mi']))
   & (df['Year of event'] == 2020)
   & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]


# In[31]:


df2.shape


# In[32]:


#remove USA from event name

df2['Event name'] = df2['Event name'].str.split('(').str.get(0)


# In[35]:


df2.head(10)


# In[37]:


#clean up Athlete age
df2['athlete_age'] = 2020 - df2['Athlete year of birth']


# In[38]:


#remove the h in athlete performance
df2['Athlete performance'] = df2['Athlete performance'].str.split(' ').str.get(0)


# In[39]:


df2.head(5)


# In[ ]:


#it is time to drop the columns we don't need for our analysis
#we are dropping the following columns:
#Athlete club, Athlete country, Athlete year of birth, Athlete Age category


# In[40]:


df2 = df2.drop(['Athlete club','Athlete country','Athlete year of birth', 'Athlete age category'], axis =1)


# In[41]:


df2.head(10)


# In[42]:


df2.shape


# In[45]:


#time to clean up null values
df2.isna().sum()


# In[46]:


df2 = df2.dropna()


# In[50]:


df2


# In[52]:


#let's remove duplicates

df2[df2.duplicated() == True]


# In[53]:


#we need to reset index or the numbering system
df2.reset_index(drop = True)


# In[55]:


#Fix the different types of data 

df2.dtypes


# In[56]:


#change the data types of Athlete average speed and athlete_age

df2['athlete_age'] = df2['athlete_age'].astype(int)
df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[57]:


df2.dtypes


# In[58]:


#Rename the columns

df2 = df2.rename(columns = {'Year of event': 'Year',
                            'Event dates': 'race_date',
                            'Event name': 'Race_name',
                            'Event distance/length': 'Distance',
                            'Event number of finishers': 'number_of_finishers',
                            'Athlete performance': 'Performance',
                            'Athlete gender': 'Gender',
                            'Athlete average speed': 'Average_speed',
                            'Athlete ID': 'Athlete_ID',
                            'Athlete age': 'Athlete_age'
                           
                           })


# In[59]:


df2.head(10)


# In[64]:


df3 = df2[['Athlete_ID','Gender','race_date', 'Distance', 'athlete_age', 'Performance', 'number_of_finishers', 'Average_speed', 'Race_name']]


# In[65]:


df3.head(10)


# In[69]:


#Chart showing the distribution of the 50miles race
sns.displot(df3[df3['Distance']=='50mi']['Average_speed'])


# In[70]:


sns.histplot(data = df3, x='Distance', hue = 'Gender')


# In[71]:


#lets see the best performing age group in the 50miles race


# In[76]:


df3.query('Distance == "50mi"').groupby('athlete_age')['Average_speed'].agg(['mean', 'count']).sort_values('mean',ascending =False).query('count>19').head(15)


# In[74]:


#The worst performing age group

df3.query('Distance == "50mi"').groupby('athlete_age')['Average_speed'].agg(['mean', 'count']).sort_values('mean',ascending =True).query('count>19').head(15)


# In[77]:


#lets look for the performance of athletes during different seasons

df3['race_month']= df3['race_date'].str.split('.').str.get(1).astype(int)


# In[78]:


df3['race_season']= df3['race_month'].apply(lambda x: 'winter' if x > 11 else 'Fall' if x > 8 else 'summer' if x > 5 else 'spring' if x > 2 else 'winter')


# In[81]:


df3.head(100)


# In[82]:


df3.groupby('race_season')['Average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False)


# In[84]:


#This is the performance of athletes during the different seasons in the 50miles race
df3.query('Distance == "50mi"').groupby('race_season')['Average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False)


# In[85]:


#This is the performance of athletes during the different seasons in the 50km race

df3.query('Distance == "50km"').groupby('race_season')['Average_speed'].agg(['mean', 'count']).sort_values('mean', ascending = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




