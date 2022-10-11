# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 10:06:07 2022

@author: hamit
"""

import streamlit as st
import pandas as pd


from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

st.write("Personal loan simulation")


st.sidebar.header("Client features")








def user_input():
    Age= st.sidebar.slider('Age',20, 70, 40)
    Experience=st.sidebar.slider('Experience', 0,43,15)
    Income=st.sidebar.slider('Income',8,224,150)
    Family=st.sidebar.slider(' Family members', 1, 6, 1)
    CCAvg=st.sidebar.slider('Average credit card spending', 0.0, 10.0, 2.0)
    Education=st.sidebar.selectbox('Education level',{'Undergraduate': 1,'Graduate':2, 'Advanced/Professional':3})
    Mortgage=st.sidebar.slider('Montgage', 0,700, 200)
    Securities_Account=st.sidebar.slider('Securities account')
    CD_Account=st.sidebar.selectbox("Depository account?",{"Yes":1, "No":0})
    
    data= {'Age':Age, 'Experience':Experience, 'Income':Income,'Family members': Family, 'CCAvg':CCAvg,'Education': Education, 'Mortgage': Mortgage, 'Securities_Account':Securities_Account,'CD_Account':CD_Account}
    Client_features=pd.DataFrame(data, index=[0])
    return Client_features

input_df= user_input() 
st.write(input_df)







# Import databse
df=pd.read_csv(r"C:\Users\hamit\Desktop\Project7\Bank_Personal_Loan_Modelling.csv")


x=df[['Age','Experience','Income', 'Family', 'CCAvg', 'Education', 'Mortgage', 'Securities Account', 'CD Account']]
#x_input=pd.concat([input_df,x],axis=0)
#x=x[:1]
x_input=input_df.append(x)

# Standardization of x_input.


y=df[['Personal Loan']]

for col in x_input :
    sc = StandardScaler()
    col= sc.fit_transform(col)
#x=x[:1]

st.subbheader('Scaled features')
st.write(x_input)

#Model classification

model=KNeighborsClassifier()
model.fit(x_input, y)   
prediction=model.predict(x_input)
    
    
st.subheader('Prediction result')  
st.write(prediction)
    
    
    
    
   
