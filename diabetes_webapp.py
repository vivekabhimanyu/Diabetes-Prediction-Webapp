

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("C:/Users/vivek abhimanyu/Documents/major_project/diabetes_model.sav", 'rb'))

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
      st.write("vidhi AI powered predictions")
      
      #getting the input dat afrom users
      
      Pregnancies = st.text_input("Number of Pregnancies : ")
      Glucose = st.text_input("Glucose levels")
      BloodPressure = st.text_input("Blood Pressure value ")
      SkinThickness = st.text_input("SkinThickness value ")
      Insulin = st.text_input("insulin level ")
      BMI = st.text_input("BMI Value ")
      DPF = st.text_input("Diabetes pedigree Function value ")
      Age = st.text_input("Age of patitent ")
      
      
      #code for prediction
      diagnosis=''
      
      #creating a buttion for prediction
      if st.button('diabetes test result'):
          diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age])
          
      st.success(diagnosis) 
      
      
      
if __name__ =='__main__':
    
    main()
    
    

      
    
    
      
      
      
      
      
      
      
      
      
      
