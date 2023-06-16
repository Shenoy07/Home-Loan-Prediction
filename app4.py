#Import
import os
os.system('pip install imblearn')
import pandas as pd
import numpy as np


import streamlit as st
import pickle
model = pickle.load(open('model.pkl','rb'))

# define a function to make predictions
def predict_loan_status(features):
    # preprocess user inputs
    
    features = np.array(features).astype(np.float64)
    # make predictions using the pre-trained model
    prediction = model.predict(features.reshape(1,-1))
    return prediction[0]

# create the web app
def main():
    # create a simple web page title
    st.title('Home Loan Approval Prediction')

    # create input fields for user to input features
    gender = st.selectbox('Gender', ['Male', 'Female'])
    married = st.selectbox('Marital Status', ['Yes', 'No'])
    dependents = st.selectbox('Number of Dependents', ['0', '1', '2', '3+'])
    education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
    applicant_income = st.number_input('Applicant Income', min_value=0)
    coapplicant_income = st.number_input('Coapplicant Income', min_value=0)
    loan_amount = st.number_input('Loan Amount', min_value=0)
    loan_term = st.number_input('Loan Term', min_value=0)
    credit_history = st.selectbox('Credit History', ['0', '1'])
    property_area = st.selectbox('Property Area', ['Urban', 'Rural','Semi'])
 
    # create a button to trigger prediction
    if st.button('Predict'):
        if self_employed == 'Yes':
            Self_Employed_No = 0
            Self_Employed_Yes = 1
        else:
            Self_Employed_No = 1
            Self_Employed_Yes = 0
        
        if education == 'Graduate':
            Education_Graduate = 1
            Education_Not_Graduate = 0
        else: 
            Education_Graduate = 0
            Education_Not_Graduate = 1
        
        # preprocess user inputs
        if property_area == 'Rural':
            Property_Area_Rural = 1
            Property_Area_Semiurban = 0  
            Property_Area_Urban = 0
        
        if property_area == 'Urban':
            Property_Area_Rural = 0
            Property_Area_Semiurban = 0  
            Property_Area_Urban = 1 
        
        if property_area == 'Semiurban':
            Property_Area_Rural = 0
            Property_Area_Semiurban = 1 
            Property_Area_Urban = 0
            
        if gender == 'Male':
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1
        
        if dependents == '0':
            Dependents_0 = 1
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 0
            
        if dependents == '1':
            Dependents_0 = 0
            Dependents_1 = 1
            Dependents_2 = 0
            Dependents_3 = 0  
            
        if dependents == '2':
            Dependents_0 = 0
            Dependents_1 = 0
            Dependents_2 = 1
            Dependents_3 = 0 
            
        if dependents == '3+':
            Dependents_0 = 0
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 1 
            
            
        if married == 'Yes':
            married_Yes = 1
            married_No = 0
        else:
            married_Yes = 1
            married_No = 0
            
        credit_history = int(credit_history)
        features = [applicant_income, coapplicant_income, loan_amount, loan_term, credit_history, Property_Area_Rural,
                    Property_Area_Semiurban, Property_Area_Urban, Gender_Female, Gender_Male, married_No, married_Yes,
                    Dependents_0, Dependents_1, Dependents_2, Dependents_3,
                    Education_Graduate, Education_Not_Graduate, Self_Employed_No, Self_Employed_Yes]
        # make predictions using the pre-trained model
        prediction = predict_loan_status(features)
        # display the prediction result
        if prediction == 'Y':
            st.success('Congratulations! Your loan is approved.')
        else:
            st.warning('Sorry, your loan is not approved.')
        # st.write('Predicted Loan Status:', prediction)

# run the web app
if __name__ == '__main__':
    main()
