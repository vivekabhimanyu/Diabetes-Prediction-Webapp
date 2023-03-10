# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:24:00 2023

@author: vivek abhimanyu
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved model

diabetes_model = pickle.load(open("trained_model.pkl","rb" ))

heart_disease_model = pickle.load(open("heart_disease_model.pkl","rb" ))

covid19_model = pickle.load(open("covid_model.pkl","rb" ))

breast_cancer_model = pickle.load(open("breast_cancer_model.pkl","rb"))

#sidebar for navigation
selected =option_menu("Multiple Disesase Prediction System",
                      options=['Home',"Diabetes","Heart","Covid-19","Breast Cancer"],
                      icons = ["house check","person","activity","bandaid","gender-female"],
                      orientation="horizontal",
                      styles={"container": {"padding": "0!important", "background-color": "#fafafa"},"icon": {"color": "orange", "font-size": "25px"},"nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "green"}})

#home vidhi predictions
if (selected =="Home"):
    #page title
    st.title("vidhi predictions") 
    

    
#diabetes predicion page
if (selected =="Diabetes"):
    #page title
    st.title("Diabets prediction using ml")
    
    #getting the input data afrom users
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies : ",min_value=0,max_value=None)
    with col2:
        Glucose = st.number_input("Glucose levels",min_value=0,max_value=199)
    with col3:
        BloodPressure = st.number_input("Blood Pressure value ",min_value=0,max_value=122)
    with col1:
        SkinThickness = st.number_input("SkinThickness value ",min_value=0,max_value=99)
    with col2:
        Insulin = st.number_input("insulin level ",min_value=0,max_value=846)
    with col3:
        BMI = st.number_input("BMI Value ",min_value=0.0,max_value=67.1)
    with col1:
        DPF = st.number_input("Diabetes pedigree Function value ",min_value=0.078,max_value=2.42)
    with col2:
        Age = st.number_input("Age of patitent ",min_value=21,max_value=81)
        
    
    #code for prediction
    diab_dis=""
    
    #creating a button for prediction
    if st.button("Diabetes Test results"):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age]])
    
        if diab_prediction[0]==1:
            diab_dis="Person is Diabetic"
        else:
            diab_dis="Person is Healthy!!!"
    st.success(diab_dis)
    
    
            
#heart disease prediction
if (selected =="Heart"):
    #page title
    st.title("heart diesase prediction using ml")
    st.caption(":violet[Predictions Simplified]....")
    
    
    #radio buttons values 
    gender_type = ["Female","Male"]
    chest_pain_type = ["typical angina", "atypical angina", "non-anginal", "asymptomatic"]
    fbs_type=["fasting blood sugar < 120 mg/dl", " fasting blood sugar > 120 mg/dl"]
    restecg_type = ["normal", "stt abnormality", "lv hypertrophy"]
    exang_type=["False","True"]
    slope_type = ["Downsloping","Flat","upsloping"]
    thal_type = ["normal","fixed defect"," reversible defect"]

   #taking input from user
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
    if Sex =='Female':
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

        
    # code for prediction
    heart_dis = ""
    #creating a button for prediction
    if(st.button('Heart Disease Test Result')):
        heart_prediction = heart_disease_model.predict([[Age,Sex,chest_pain,trestbps,chol,fbs,restecg,thalach,exang,oldpeek,slope,ca,thal]])
        if (heart_prediction[0]== 0):
            heart_dis='The Person is Healthy!!!'
        else:
            heart_dis='The Person has Heart Disease'
    st.success(heart_dis)
#covid 19 prediction
if (selected =="Covid-19"):
    #page title
    st.title("covid19 prediction using ml")
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
    covid_dis=''
  
  #creating a buttion for prediction
    if st.button('covid-19 test results'):
       covid_prediction=covid19_model.predict([[Age,BMI,Diabetes,Cardio_Vascular_Diseases,Sickle_cell_diesases,Immuno_deficiency_disease,Down_syndrome,cancer,Chronic_Respiratory_disease,Hypertension,Vaccinated]])
       if covid_prediction[0]==0:
          covid_dis="Person is healthy"
       else:
          covid_dis="person effected by covid-19"
    st.success(covid_dis) 

if (selected == "Breast Cancer"):
    #page title
    st.title("Breast Cancer Prediction using ML")
    #getting the inputs from the users
    #columns for inpt fields
    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        mean_radius = st.number_input("Mean radius ",min_value = 6.0,max_value = 28.0,format="%.2f")
    with col2:
        mean_texture = st.number_input("Mean texture ",min_value = 9.0,max_value = 40.0,format="%.2f")
    with col3:
         mean_perimeter = st.number_input("Mean radius ",min_value = 43.0,max_value =190.0 ,format="%.2f")
    with col4:
         mean_area = st.number_input("Mean area ",min_value = 143.0,max_value = 2500.0,format= "%.2f")
    with col5:
        mean_smoothness = st.number_input("Mean smoothness ",min_value =0.05263 ,max_value=0.16340 , format = "%.5f")
    with col1:
         mean_compactness = st.number_input("Mean compactness ",min_value =0.01938,max_value= 0.34540, format = "%.5f")
    with col2:
         mean_concavity = st.number_input("Mean concavity ",min_value =0.0000 ,max_value=0.4268 , format = "%.4f")
    with col3:
         mean_concave_points = st.number_input("Mean concave points ",min_value =0.00000 ,max_value= 0.20120, format = "%.5f")
    with col4:
        mean_symmetry = st.number_input("Mean symmetry ",min_value =0.1060 ,max_value=0.3040, format = "%.4f")
    with col5:
         mean_fractal_dimension = st.number_input("Mean fractal dimension ",min_value = 0.04996,max_value=0.09744, format = "%.5f")
    with col1:
         error_radius = st.number_input("Radius error " , min_value = 0.1115, max_value = 2.8730 , format = "%.4f")
    with col2:
        error_texture = st.number_input("Texture error " , min_value =0.3602 , max_value = 4.8850 , format = "%.4f")
    with col3:
         error_perimeter = st.number_input("Perimeter error " , min_value = 0.757 , max_value =21.980  , format = "%.3f")
    with col4:
         error_area = st.number_input("Area error " , min_value = 6.802, max_value =542.200  , format = "%.3f")
    with col5:
         error_smoothness = st.number_input("Smoothness error " , min_value =0.001713 , max_value = 0.031130 , format = "%.6f")
    with col1:
        error_compactness = st.number_input("Compactness error " , min_value = 0.002252, max_value = 0.125400 , format = "%.6f")
    with col2:
        error_concavity= st.number_input("Concavvity error " , min_value =0.00000 , max_value = 0.39600 , format = "%.5f")
    with col3:
        error_concave_points = st.number_input("Concave points error " , min_value = 0.0000, max_value = 0.05279 , format = "%.5f")
    with col4:
        error_symmetry = st.number_input("Symmetry error " , min_value = 0.007882, max_value = 0.078950 , format = "%.6f")
    with col5:
        error_fractal_dimension = st.number_input("Fractal dimension error " , min_value = 0.000895, max_value =0.029840  , format = "%.6f")
    with col1:
        worst_radius = st.number_input("Worst radius ",min_value =7.930 ,max_value=36.040,format= "%.3f")
    with col2:
        worst_texture = st.number_input("Worst  texture ",min_value = 12.02 ,max_value= 49.54,format= "%.2f")
    with col3:
        worst_perimeter = st.number_input("Worst perimeter ",min_value = 50.40, max_value= 251.20,format= "%.2f")
    with col4:
        worst_area = st.number_input("Worst area ",min_value =185.20 ,max_value= 4254.00,format= "%.2f")
    with col5:
        worst_smoothness = st.number_input("Worst smoothness ",min_value = 0.07117, max_value= 0.22260, format= "%.5f")
    with col1:
        worst_compactness = st.number_input("Worst  compactness ",min_value = 0.02729,max_value= 1.05800,format= "%.5f")
    with col2:
        worst_concavity = st.number_input("Worst concavity ",min_value =0.00000 , max_value= 1.25200, format= "%.5f")
    with col3:
        worst_concave_points = st.number_input("Worst concave points ",min_value =0.0000, max_value=1.2910, format= "%.4f")
    with col4:
        worst_symmetry = st.number_input("Worst symmetry ",min_value = 0.1565, max_value=0.6638, format= "%.4f")
    with col5:
        worst_fractal_dimension = st.number_input("Worst fractal dimension ",min_value =0.05504 ,max_value=0.20750,format= "%.5f")
    
    #code for prediction
    bst_cnr = ""
    #creating a button for prediction
    if(st.button('Breast Cancer Results')):
        bst_pre = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,
                                          error_radius,error_texture,error_perimeter,error_area,error_smoothness,error_compactness,error_concavity,error_concave_points,error_symmetry,error_fractal_dimension,
                                          worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        if bst_pre[0]==0:
            bst_cnr=" Malignant Tumor Found" +" "+ "&" +" "+ " Consult Surgeon Immediately!!!! "
            bst_cnr="high risk"
        else:
            bst_cnr=" Benign Tumor Found" +" "+ "&" +" " +"Better To Consult Doctor"
        
    st.success(bst_cnr)


