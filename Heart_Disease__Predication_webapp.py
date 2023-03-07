# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:37:20 2023

@author: Govardhan
"""
import numpy as np
import pickle
import streamlit as st



loaded_model = pickle.load(open('heart_disease_model.pkl','rb'))
                                

#creating a function for prediction
def heart_predication_model(input_data):
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Person doesnot have any heart disease'
    else:
      return 'The person has heart disease'
      
  


def main():
    
    #radio buttons values 
    gender_type = ["Female","Male"]
    chest_pain_type = ["typical angina", "atypical angina", "non-anginal", "asymptomatic"]
    fbs_type=["fasting blood sugar < 120 mg/dl", " fasting blood sugar > 120 mg/dl"]
    restecg_type = ["normal", "stt abnormality", "lv hypertrophy"]
    exang_type=["False","True"]
    slope_type = ["Downsloping","Flat","upsloping"]
    thal_type = ["normal","fixed defect"," reversible defect"]
    
    
    
    #taking input from user
    
    st.title("Heart Disease Prediction Web App")
    
    Age = st.number_input("Age of patient :",min_value=29,max_value=130)
    
    Sex = st.radio("Select Gender :",gender_type)
    
    chest_pain = st.radio("Select Chest Pain type :",chest_pain_type)
    
    trestbps = st.number_input("Trestbps resting blood pressure :",min_value=94,max_value=200)
    
    chol = st.number_input("Serum cholesterol in mg/dl :",min_value=126,max_value=564)
    
    fbs =  st.radio("Fasting blood sugar type :",fbs_type)
    
    restecg = st.radio("Resting electrocardiographic results :",restecg_type)
    
    thalach = st.number_input("Maximum heart rate achieved(thalach) :",min_value=70,max_value = 202)
    
    exang = st.radio(" Exercise induced angina :",exang_type)
    
    oldpeek = st.number_input("Oldpeek value : ",min_value= 0,max_value=7)
    
    slope = st.radio("the slope of the peak exercise ST segment :",slope_type)
    
    ca = st.number_input("number of major vessels (0-3) colored by fluoroscopy",min_value=0,max_value = 3)
    
    thal = st.radio("Thal :" ,thal_type)
    
    #assigning values for gender 
    if Sex=='Female':
        Sex = 0
    else:
        Sex = 1
        
    # assigning values for chest pain
    if chest_pain == "typical angina":
        chest_pain = 0
    elif chest_pain == "atypical angina":
        chest_pain = 1
    elif chest_pain == "non-anginal":
        chest_pain = 2
    else:
        chest_pain = 3
        
        
    # assigning values for fbs
    if fbs == "fasting blood sugar < 120 mg/dl":
        fbs = 0
    else :
        fbs = 1
    
    # asssigning values for restecg
    if restecg == "normal":
        restecg = 0
    elif restecg == "stt abnormality":
        restecg = 1
    else:
        restecg = 2
        
    #assigning values to exang
    if exang == "True":
        exang = 1
    else:
        exang = 0
    
    
    if slope == "Flat":
        slope =  1
    elif slope == "upsloping" :
        slope =  2
    else:
        slope = 0
    
    if thal == 'normal' :
        thal = 0
    elif thal == 'fixed defect':
        thal =  1
    else :
        thal =0
    
    result = ""
    if(st.button('Heart Disease Result')):
        result = heart_predication_model([Age,Sex,chest_pain,trestbps,chol,fbs,restecg,thalach,exang,oldpeek,slope,ca,thal])
        
    st.success(result)
                                        
    
if __name__ =='__main__':
    
    main()
