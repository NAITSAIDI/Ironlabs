# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:37:05 2022

@author: hamit
"""

import streamlit as st
import pandas as pd
from PIL import Image
import datetime

showPyplotGlobalUse = False

# Insert airbnb image

image = Image.open(r'C:\Users\hamit\Desktop\PROJECT5\airbnb2.JPG')

st.image(image, caption='airbnb')


# streamlit charts

#sst.write('# Project 5')
st.write('## airbnb New York') 
#st.text(' Airbnb data analysis')
           
                 


    
 # airbnb app   
    
    
option = st.selectbox('Please, select a neighborhood group',('Queens', 'Manhattan', 'Staten_Island', ' Bronx', 'Brooklyn'))
room_type=st.selectbox('Please, seclect your room type', ('Private room', 'Entire home/apt', 'Shared room', ' Hotel room'))
arrival = st.sidebar.date_input('Arrival', datetime.date(2022,8,27)) 
departure = st.sidebar.date_input(' Departure', datetime.date(2023,12,30))
instant_bookable= st.sidebar.selectbox("Select yes or no",["Yes", "No"])
#st.write(f"You selected {selectbox}")
#st.write('You selected:', option)








if option=='Queens': 
    def select():
        period=st.sidebar.slider('number of days', 1, 365, 30)
        price=st.sidebar.slider('Price', 50, 1200, 443)
        Minimum_Nights=st.sidebar.slider('Minimum Nights', 1,365, 443)
        total_price =st.write('The amount to pay is', round(price*period), '$')
        fees =st.write('The amount of service fee is', round(price*0.2), '$')
        
        data= {"price":price,"Minimum_Nights":Minimum_Nights, 'number of days':period }
        
        select = pd.DataFrame(data, index=[0]) 
        return select
    
elif option=='Manhattan':
    def select():
        period=st.sidebar.slider('number of days', 1, 365, 30)
        price=st.sidebar.slider('Price', 50, 1200, 443)
        Minimum_Nights=st.sidebar.slider('Minimum_Nights', 1, 365, 443)
        total_price =st.write('The amount to pay is', round(price*period), '$')
        fees =st.write('The amount of service fee is', round(price*0.2), '$')
        
        data={"price":price,"Minimum_Nights":Minimum_Nights, 'number of days':period, 'fees':fees}
        select = pd.DataFrame(data, index=[0]) 
        return select



elif option=='Staten_Island':
    def select():
        period=st.sidebar.slider('number of days', 1, 365, 30)
        price=st.sidebar.slider('Price', 50, 1200, 443)
        Minimum_Nights=st.sidebar.slider('Minimum_Nights', 1, 999, 443)
        total_price =st.write('The amount to pay is', round(price*period), '$')
        fees =st.write('The amount of service fee is', round(price*0.2), '$')
        
        data={"price":price,"Minimum_Nights":Minimum_Nights, 'number of days':period, 'fees':fees}
        
        select = pd.DataFrame(data, index=[0]) 
        return select
    
elif option=='Bronx':
    def select():
        period=st.sidebar.slider('number of days', 1, 365, 30)
        price=st.sidebar.slider('Price', 50, 1200, 443)
        Minimum_Nights=st.sidebar.slider('Minimum_Nights', 1, 365, 443)
        total_price =st.write('The amount to pay is', round(price*period), '$')
        fees =st.write('The amount of service fee is', round(price*0.2), '$')
        
        data={"price":price,"Minimum_Nights":Minimum_Nights, 'number of days':period, 'fees':fees}
        
        select = pd.DataFrame(data, index=[0]) 
        return select
    
elif option=='Brooklyn':
    def select():
        period=st.sidebar.slider('number of days', 1, 365, 30)
        price=st.sidebar.slider('Price', 50, 1200, 443)
        Minimum_Nights=st.sidebar.slider('Minimum_Nights', 1, 365,30)
        total_price =st.write('The amount to pay is', round(price*period), '$')
        fees =st.write('The amount of service fee is', round(price*0.2), '$')
        
        data={"price":price,"Minimum_Nights":Minimum_Nights, 'number of days':period, 'fees':fees}
        
        select = pd.DataFrame(data, index=[0]) 
        return select
    
    
    
    
df= select()  
st.subheader('Find the price in each neighborhood group')    
st.write(df)        
    
    
   
       




