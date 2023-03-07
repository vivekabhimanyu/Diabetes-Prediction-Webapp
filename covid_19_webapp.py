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
      st.title("Covid-19 prediction WebApp")
      st.caption(":violet[Predictions Simplified]....")


      #radio button values
      Diabetes=["Yes","No"]
      Cardio_Vascular_Diseases=["Yes","No"]
      Sickle_cell_diesases=["Yes","No"]
      Immuno_deficiency_disease=["Yes","No"]
      Down_syndrome=["Yes","No"]
      cancer=["Yes","No"]
      Chronic_Respiratory_disease=["Yes","No"]
      Hypertension=["Yes","No"]
      Vaccinated=["Yes","No"]

      #getting the input dat afrom users
      #0--> no and 1---> health issues is there
      
      Age = st.number_input("Enter Your Age : ",min_value=10,max_value=100)
      BMI = st.number_input("Enter Your BMI : ",min_value=10,max_value=80)
      Diabetes = st.radio("Do You Have Diabetes ?? : ",Diabetes)
      Cardio_Vascular_Diseases = st.radio("Do You Have cardio vascular disease ??",Cardio_Vascular_Diseases)
      Sickle_cell_diesases = st.radio("Do You Have Sickle_cell_diesases ?",Sickle_cell_diesases)
      Immuno_deficiency_disease = st.radio("Do You Have Immuno_deficiency_disease ",Immuno_deficiency_disease)
      Down_syndrome = st.radio("Do You Have Down_syndrome ?",Down_syndrome)
      cancer = st.radio("Do You Have Cancer ?",cancer)
      Chronic_Respiratory_disease = st.radio("Do You Have Chronic_Respiratory_disease ?",Chronic_Respiratory_disease)
      Hypertension = st.radio("Do You Have Hypertension ?",Hypertension)
      Vaccinated = st.radio(" Are You Vaccinated ?",Vaccinated)

      #Assigning values for diseases
      if Diabetes=='Yes':
          Diabetes=1
      else:
          Diabetes=0
      if Cardio_Vascular_Diseases=='Yes':
          Cardio_Vascular_Diseases=1
      else:
          Cardio_Vascular_Diseases=0
      if Sickle_cell_diesases=='Yes':
          Sickle_cell_diesases=1
      else:
          Sickle_cell_diesases=0
      if Immuno_deficiency_disease=='Yes':
          Immuno_deficiency_disease=1
      else:
          Immuno_deficiency_disease=0
      if Down_syndrome=='Yes':
          Down_syndrome=1
      else:
          Down_syndrome=0
      if cancer=='Yes':
          cancer=1
      else:
          cancer=0
      if Chronic_Respiratory_disease=='Yes':
          Chronic_Respiratory_disease=1
      else:
          Chronic_Respiratory_disease=0
      if Hypertension=='Yes':
          Hypertension=1
      else:
          Hypertension=0
      if Vaccinated=='Yes':
          Vaccinated=1
      else:
          Vaccinated=0
      
      #code for prediction
      diagnosis=''
      
      #creating a buttion for prediction
      if st.button('covid-19 test result'):
          diagnosis=covid_prediction([Age,BMI,Diabetes,Cardio_Vascular_Diseases,Sickle_cell_diesases,Immuno_deficiency_disease,Down_syndrome,cancer,Chronic_Respiratory_disease,Hypertension,Vaccinated])
          
      st.success(diagnosis) 
      
      
      
if __name__ =='__main__':
    
    main()

