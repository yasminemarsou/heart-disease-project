from pyexpat import model
import numpy as np
import joblib
import streamlit as st
from streamlit_option_menu import option_menu
filename = 'D:/PYTHON/heart disease project/app/trained_model.sav'
#loading the saved model
loaded_model = joblib.load(open(filename, 'rb'))
joblib.dump(loaded_model, filename)

#creating function for prediction
def heart_disease_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return "heart disease negative"
    else:
        return "heart disease positive"
    
def main():

    #giving a title
    st.title('heart disease web app')

    #getting the input data from the user

    age;sex;cp;trestbps;cho;fbs;restecg;thalach;exang;oldpeak;slope;ca;thal;num

    age = st.text_input('your age')
    sex = st.text_input('gender')
    cp = st.text_input('cp level')
    trestbps= st.text_input('trestbps level')
    cho = st.text_input('cholesterole')
    fbs = st.text_input('fbs level')
    restecg = st.text_input('restecg level')
    thalach = st.text_input('thalach level')
    exang = st.text_input('exang level')
    oldpeak =st.text_input('oldpeak level')
    slope = st.text_input('slope level')
    ca = st.text_input ('ca level')
    thal = st.text_input('thal level')
    num =st.text_input('num')

    #code for prediction
    diagnosis = ''

    #creating a button for prediction

    if st.button('heart diseas results'):
        diagnosis = heart_disease_prediction([age, sex, cp, trestbps, cho, fbs, restecg, thalach,exang, oldpeak,slope, ca, thal, num])
    st.success(diagnosis)
if __name__ == '__main__ ':
    main()

