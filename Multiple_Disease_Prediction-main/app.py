import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

# Page config
st.set_page_config(
    page_title="Multiple Disease Prediction",
    page_icon="🏥",
    layout="wide"
)

# Loading the saved models
try:
    diabetes_model = pickle.load(open('models/new_diabetes.sav', 'rb'))
    heart_disease_model = pickle.load(open('models/new_heart.sav', 'rb'))
    pneumonia_model = load_model('models/pneumonia.hdf5')
    brain_tumor_model = load_model('models/brain_tumor.hdf5')
except Exception as e:
    st.error(f"Error loading models: {e}")

# Sidebar for navigation
selected = option_menu('Multiple Disease Prediction Dashboard',
                       ['Home', 'Diabetes Prediction',
                        'Heart Disease Prediction', "Pneumonia Detection", "Brain Tumour Detection"],
                       icons=['house-fill', 'capsule-pill', 'heart-pulse-fill', 'lungs', 'brain'],
                       menu_icon='clipboard2-pulse',
                       orientation='horizontal')

# Home Page
if selected == 'Home':
    st.title('Multiple Disease Prediction using Machine Learning')
    st.image('assets/main_banner.gif')

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('💊 Diabetes Prediction using ML')
    col1, col2 = st.columns(2)
    with col1:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
    with col2:
        BMI = st.text_input('BMI value')
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[float(Glucose), float(Insulin), float(BMI), float(Age)]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except:
            diab_diagnosis = 'Please enter valid numerical values'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('❤️ Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        text = st.selectbox('Chest Pain', ('No Pain', 'Low Pain', 'Moderate Pain', 'High Pain'))
        cp = {'No Pain': 0, 'Low Pain': 1, 'Moderate Pain': 2, 'High Pain': 3}[text]
    with col3:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col1:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')
    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[int(age), cp, float(chol), float(thalach), float(oldpeak), int(ca)]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except:
            heart_diagnosis = 'Please enter valid numerical values'
    st.success(heart_diagnosis)

# Pneumonia Detection Page
if selected == "Pneumonia Detection":
    st.title("👨‍⚕️ Pneumonia Detection using ML")
    file = st.file_uploader("Please upload an X-ray file", type=["jpg", "png"])
    pneumonia_diagnosis = ''
    
    if file is not None:
        try:
            img = tf.keras.utils.load_img(file, target_size=(64, 64))
            x = tf.keras.utils.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            img_data = preprocess_input(x)
        
            if st.button("Pneumonia Test Result"):
                classes = pneumonia_model.predict(img_data)
                result = classes[0][0]
                if result == 0:
                    pneumonia_diagnosis = "The person has Pneumonia"
                else:
                    pneumonia_diagnosis = "The person does not have Pneumonia"
        except Exception as e:
            pneumonia_diagnosis = f"Error processing image: {e}"
    st.success(pneumonia_diagnosis)

# Brain Tumour Detection Page
if selected == "Brain Tumour Detection":
    st.title("🧠 Brain Tumour Detection using ML")
    file = st.file_uploader("Please upload an MRI file", type=["jpg", "png"])
    tumour_diagnosis = ''
    
    if file is not None:
        try:
            img = tf.keras.utils.load_img(file, target_size=(64, 64))
            x = tf.keras.utils.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            img_data = preprocess_input(x)
            
            if st.button("Tumour Test Result"):
                classes = brain_tumor_model.predict(img_data)
                result = classes[0][0]
                if result == 0:
                    tumour_diagnosis = "The person has a Brain Tumour"
                else:
                    tumour_diagnosis = "The person does not have a Brain Tumour"
        except Exception as e:
            tumour_diagnosis = f"Error processing image: {e}"
    st.success(tumour_diagnosis)
