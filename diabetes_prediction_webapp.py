# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 02:28:30 2023

@author: ARVI
"""

import numpy as np
import pickle
import streamlit as st
import string

# loading the saved model
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

#creating a function for prediction
def diabetes_prediction(input_data):
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'non diabetic'
    else:
      return 'The person is diabetic'
      
  
    
  
def main():
      #making title
      st.title("Diabetes prediction Web App")
      st.latex("vidhi  ai powered predictions")
      
      #getting the input dat afrom users
      
      Pregnancies = st.number_input("Number of Pregnancies : ",min_value=0,max_value=None)
      Glucose = st.number_input("Glucose levels",min_value=0,max_value=199)
      BloodPressure = st.text_number("Blood Pressure value ",min_value=0,max_value=122)
      SkinThickness = st.text_number("SkinThickness value ",min_value=0,max_value=99)
      Insulin = st.text_number("insulin level ",min_value=0,max_value=846)
      BMI = st.text_number("BMI Value ",min_value=0.0,max_value=67.1)
      DPF = st.text_number("Diabetes pedigree Function value ",min_value=0.078,max_value=2.42)
      Age = st.text_number("Age of patitent ",min_value=21,max_value=81)
      
      
      #code for prediction
      diagnosis=''
      
      #creating a buttion for prediction
      if st.button('diabetes test result'):
          diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age])
          
      st.success(diagnosis) 
      
      
      
if __name__ =='__main__':
    
    main()
      
    
    
      
      
      
      
      
      
      
      
      
      
