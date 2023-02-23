import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('Random_forest_model.pkl', 'rb'))
df = pd.read_csv('heart.csv')


st.title('Heart Disease Prediction')

age = st.sidebar.number_input('Enter your age: ')
sex  = st.sidebar.selectbox('Sex',(0,1))
cp = st.sidebar.selectbox('Chest pain type', (0, 1, 2, 3))
tres = st.sidebar.number_input('Resting blood pressure: ')
chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
fbs = st.sidebar.selectbox('Fasting blood sugar', (0, 1))
res = st.sidebar.number_input('Resting electrocardiographic results: ')
tha = st.sidebar.number_input('Maximum heart rate achieved: ')
exa = st.sidebar.selectbox('Exercise induced angina: ', (0, 1))
old = st.sidebar.number_input('oldpeak ')
slope = st.sidebar.number_input('he slope of the peak exercise ST segmen: ')
ca = st.sidebar.selectbox('number of major vessels', (0, 1, 2, 3))
thal = st.sidebar.selectbox('thal', (0, 1, 2))

result=''
if st.button('Predict'):
    input = pd.DataFrame([[age,sex,cp,tres,chol,fbs,res,tha,exa,old,slope,ca,thal]],columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
    prediction = model.predict(input)
    if prediction==0:
        result="You do not have a heart disease"
    else:
        result="You have a heart disease"


st.success(result)
