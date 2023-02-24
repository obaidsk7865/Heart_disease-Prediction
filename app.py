import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('Random_forest_model.pkl', 'rb'))
df = pd.read_csv('heart.csv')


st.title('Heart Disease Prediction')

age = st.number_input('Enter your age: ')
sex  = st.selectbox('Sex',(0,1))
cp = st.selectbox('Chest pain type', (0, 1, 2, 3))
tres = st.number_input('Resting blood pressure: ')
chol = st.number_input('Serum cholestoral in mg/dl: ')
fbs = st.selectbox('Fasting blood sugar', (0, 1))
res = st.number_input('Resting electrocardiographic results: ')
tha = st.number_input('Maximum heart rate achieved: ')
exa = st.selectbox('Exercise induced angina: ', (0, 1))
old = st.number_input('oldpeak ')
slope = st.number_input('he slope of the peak exercise ST segmen: ')
ca = st.selectbox('number of major vessels', (0, 1, 2, 3))
thal = st.selectbox('thal', (0, 1, 2))

result=''
if st.button('Predict'):
    input = pd.DataFrame([[age,sex,cp,tres,chol,fbs,res,tha,exa,old,slope,ca,thal]],columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
    prediction = model.predict(input)
    if prediction==0:
        result="You do not have a heart disease"
    else:
        result="You have a heart disease"


st.success(result)
