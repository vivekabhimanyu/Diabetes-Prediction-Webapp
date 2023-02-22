# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 02:28:30 2023

@author: ARVI
"""

import numpy as np
import pickle
import streamlit as st
import string

# Adding the background image
page_bg_image="""
<style>
[data-testid="stAppViewContainer"] {background-color: #e5e5f7;
opacity: 0.8;
background-image: radial-gradient(circle at center center, #444cf7, #e5e5f7), repeating-radial-gradient(circle at center center, #444cf7, #444cf7, 10px, transparent 20px, transparent 10px);
background-blend-mode: multiply;}
</style>
"""
st.markdown=(page_bg_image,unsafe_allow_html=True)
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
      st.latex("Simplified Solutions.......")
      
      #getting the input dat afrom users
      
      Pregnancies = st.number_input("Number of Pregnancies : ",min_value=0,max_value=None)
      Glucose = st.number_input("Glucose levels",min_value=0,max_value=199)
      BloodPressure = st.number_input("Blood Pressure value ",min_value=0,max_value=122)
      SkinThickness = st.number_input("SkinThickness value ",min_value=0,max_value=99)
      Insulin = st.number_input("insulin level ",min_value=0,max_value=846)
      BMI = st.number_input("BMI Value ",min_value=0.0,max_value=67.1)
      DPF = st.number_input("Diabetes pedigree Function value ",min_value=0.078,max_value=2.42)
      Age = st.number_input("Age of patitent ",min_value=21,max_value=81)
      
      
      #code for prediction
      diagnosis=''
      
      #creating a buttion for prediction
      if st.button('diabetes test result'):
          diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age])
          
      st.success(diagnosis) 
      
      
      
if __name__ =='__main__':
    
    main()
      
    
    
      
      
      
      
      
      
      
      
      
      
