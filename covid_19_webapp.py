# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 02:28:30 2023

@author: ARVI
"""

import numpy as np
import pickle
import streamlit as st
import string

# loading the saved model
loaded_model = pickle.load(open("covid_model.pkl", 'rb'))

#creating a function for prediction
def covid_prediction(input_data):
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return ' Congrats!You are now Safe & Healthy'
    else:
      return 'OOPS!!! You Are in Risk Of Covid-19'
      
  
    
  
def main():
      #making title
      st.title("Covid-19 Risk Analyser")
      st.caption(":violet[Predictions Simplified]....")
      
      #getting the input dat afrom users
      #0--> no and 1---> health issues is there
      
      Age = st.number_input("Enter Your Age : ",min_value=0,max_value=100)
      BMI = st.number_input("Enter Your BMI : ",min_value=0,max_value=80)
      st.subheader(":red[If You Are Suffering with Disease Press 1]")
      Diabetes = st.number_input("Do You Have Diabetes ?? : ",min_value=0,max_value=1)
      Cardio_Vascular_Diseases = st.number_input("Do You Have cardio vascular disease ??",min_value=0,max_value=1)
      Sickle_cell_diesases = st.number_input("Do You Have Sickle_cell_diesases ?",min_value=0,max_value=1)
      Immuno_deficiency_disease = st.number_input("Do You Have Immuno_deficiency_disease ",min_value=0,max_value=1)
      Down_syndrome = st.number_input("Do You Have Down_syndrome ?",min_value=0,max_value=1)
      cancer = st.number_input("Do You Have Cancer ?",min_value=0,max_value=1)
      Chronic_Respiratory_disease = st.number_input("Do You Have Chronic_Respiratory_disease ?",min_value=0,max_value=1)
      Hypertension = st.number_input("Do You Have Hypertension ?",min_value=0,max_value=1)
      Vaccinated = st.number_input(" Are You Vaccinated ?",min_value=0,max_value=1)
      
      
      #code for prediction
      diagnosis=''
      
      #creating a buttion for prediction
      if st.button('covid-19 test result'):
          diagnosis=covid_prediction([Age,BMI,Diabetes,Cardio_Vascular_Diseases,Sickle_cell_diesases,Immuno_deficiency_disease,Down_syndrome,cancer,Chronic_Respiratory_disease,Hypertension,Vaccinated])
          
      st.success(diagnosis) 
      
      
      
if __name__ =='__main__':
    
    main()

