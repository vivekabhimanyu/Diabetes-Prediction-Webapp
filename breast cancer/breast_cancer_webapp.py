# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:22:01 2023

@author: Govardhan
"""
import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("breast cancer/breast_cancer_model.pkl",'rb'))

def breast_cancer_prediction(input_data):
    #changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are prediction for one as instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if(prediction[0]==0):
        return "The breast cancer is Malignant"
    else:
        return "The brease cancer is benign"


def main():
   st.title("Breast cancer Prediction")
     
   # taking input from user (mean values :)
   mean_radius = st.number_input("Mean radius :",min_value = 6.0,max_value = 28.0,format="%.2f")
   mean_texture = st.number_input("Mean texture :",min_value = 9.0,max_value = 40.0,format="%.2f")
   mean_perimeter = st.number_input("Mean radius :",min_value = 43.0,max_value =190.0 ,format="%.2f")
   mean_area = st.number_input("Mean area :",min_value = 143.0,max_value = 2500.0,format= "%.2f")
   mean_smoothness = st.number_input("Mean smoothness :",min_value =0.05263 ,max_value=0.16340 , format = "%.5f")
   mean_compactness = st.number_input("Mean campactness :",min_value =0.01938,max_value= 0.34540, format = "%.5f")
   mean_concavity = st.number_input("Mean concavity :",min_value =0.0000 ,max_value=0.4268 , format = "%.4f")
   mean_concave_points = st.number_input("Mean concave points :",min_value =0.00000 ,max_value= 0.20120, format = "%.5f")
   mean_symmetry = st.number_input("Mean symmetry :",min_value =0.1060 ,max_value=0.3040, format = "%.4f")
   mean_fractal_dimension = st.number_input("Mean fractal dimension :",min_value = 0.04996,max_value=0.09744, format = "%.5f")
   
   
   #taking input from user (error values : )   
   error_radius = st.number_input("Radius error :" , min_value = 0.1115, max_value = 2.8730 , format = "%.4f")
   error_texture = st.number_input("Texture error :" , min_value =0.3602 , max_value = 4.8850 , format = "%.4f")
   error_perimeter = st.number_input("Perimeter error :" , min_value = 0.757 , max_value =21.980  , format = "%.3f")
   error_area = st.number_input("Area error :" , min_value = 6.802, max_value =542.200  , format = "%.3f")
   error_smoothness = st.number_input("Smoothness error :" , min_value =0.001713 , max_value = 0.031130 , format = "%.6f")
   error_compactness = st.number_input("Compactness error :" , min_value = 0.002252, max_value = 0.125400 , format = "%.6f")
   error_concavity= st.number_input("Concavvity error :" , min_value =0.00000 , max_value = 0.39600 , format = "%.5f")
   error_concave_points = st.number_input("Concave points error :" , min_value = 0.0000, max_value = 0.05279 , format = "%.5f")
   error_symmetry = st.number_input("Symmetry error :" , min_value = 0.007882, max_value = 0.078950 , format = "%.6f")
   error_fractal_dimension = st.number_input("Fractal dimension error :" , min_value = 0.000895, max_value =0.029840  , format = "%.6f")

   
   # taking input from user (worst values :)
   worst_radius = st.number_input("Worst radius :",min_value =7.930 ,max_value=36.040,format= "%.3f")
   worst_texture = st.number_input("Worst  texture:",min_value = 12.02 ,max_value= 49.54,format= "%.2f")
   worst_perimeter = st.number_input("Worst perimeter :",min_value = 50.40, max_value= 251.20,format= "%.2f")
   worst_area = st.number_input("Worst area :",min_value =185.20 ,max_value= 4254.00,format= "%.2f")
   worst_smoothness = st.number_input("Worst smoothness :",min_value = 0.07117, max_value= 0.22260, format= "%.5f")
   worst_compactness = st.number_input("Worst  compactness :",min_value = 0.02729,max_value= 1.05800,format= "%.5f")
   worst_concavity = st.number_input("Worst concavity :",min_value =0.00000 , max_value= 1.25200, format= "%.5f")
   worst_concave_points = st.number_input("Worst concave points :",min_value =0.0000, max_value=1.2910, format= "%.4f")
   worst_symmetry = st.number_input("Worst symmetry :",min_value = 0.1565, max_value=0.6638, format= "%.4f")
   worst_fractal_dimension = st.number_input("Worst fractal dimension :",min_value =0.05504 ,max_value=0.20750,format= "%.5f")
   
   result = ""
   if(st.button('Breast Cancer Result')):
       result = breast_cancer_prediction([mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,
                                          error_radius,error_texture,error_perimeter,error_area,error_smoothness,error_compactness,error_concavity,error_concave_points,error_symmetry,error_fractal_dimension,
                                          worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension])
       
        
   st.success(result)
   
   

if __name__ == '__main__':
    main()
