# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 02:54:18 2022

@author: hamit
"""
showPyplotGlobalUse = False

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.express as px

showPyplotGlobalUse = False
image = Image.open(r'C:\Users\hamit\Desktop\PROJECT5\airbnb.JPG')

st.image(image, caption='airbnb')


st.write('## airbnb New York')



# File upload



df = pd.read_csv(r'C:\Users\hamit\Desktop\PROJECT5\cleaned_final.csv')
df=pd.DataFrame(df)
st.header('airbnb Dataset desciption')
st.write(df.describe())
st.header('Header Aibnb Dataframe')
st.write(df.head())
st.write(df.shape)
st.header('Price/fees')


#Plots

## Scatter plot long/lat, neighborhood group
plt.figure(figsize=(12,10))
sns.scatterplot(df['long'],df['lat'],hue=df['neighbourhood_group'])
plt.ioff()
plt.show()
st.pyplot();  



##Scatter plot price/fees
fig, ax = plt.subplots(1,1)
ax.scatter(x=df['price_per_night'], y=df['service_fee'])
ax.set_xlabel('Price')
ax.set_ylabel('Fees')
st.pyplot(fig); 
    
## Pie chart

fig=plt.figure(figsize=(8,10))
keys=('Private room', 'Entire home/apt', 'Shared room', 'Hotel room')
colors= sns.color_palette('bright')
plt.pie(df['room_type'].value_counts(), labels=keys, autopct='%.0f%%',shadow=True,wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},explode=[0,0.1,0.1,0], colors=colors)
st.pyplot(fig)



## Count plot  neighbourhood
fig2=plt.figure(figsize=(16,10))
sns.countplot(df['neighbourhood_group'], palette="plasma")
st.pyplot(fig2)  



## Scatter plt long/lat , room type (interactve)
room_type_option=df['room_type'].unique().tolist()
room_type=st.sidebar.selectbox('Seclect your room type', room_type_option)
df1=df[df['room_type']==room_type]
plt.figure(figsize=(12,10))
sns.scatterplot(df['long'],df['lat'],hue=df1['room_type'])
plt.ioff()
plt.show()
st.pyplot(); 


## Scatter plot long/lat , price (interactve)

price_per_night_option=df['price_per_night'].unique().tolist()
price_per_night=st.sidebar.slider('Seclect your price', min(price_per_night_option), max(price_per_night_option),80)
#price_per_night= st.sidebar.slider('Price:',  min(price_per_night_option), max(price_per_night_option),value= (min(price_per_night_option), max(price_per_night_option)))
df2=df[df['price_per_night']==price_per_night]
sns.scatterplot(df['long'],df['lat'],hue= df2['price_per_night'])
plt.ioff()
plt.show() 
st.pyplot(); 




