import streamlit as st 
from streamlit_lottie import st_lottie
import json
import requests


def app():
    st.title("Welcome to MediPredict")
    st.subheader("Hi, I am MediPredict :wave:")
    st.title("A Machine Learning Prediction Application")
    st.write("We help you to Predict whether you have following diseases or not")
    col1, col2 = st.columns(2)  
    with col1:
        st.link_button("Diabetes" , "https://en.wikipedia.org/wiki/Diabetes")  
    with col2:
        st.link_button("Pneumonia", "https://en.wikipedia.org/wiki/Pneumonia")
    with col1:
        st.link_button("Brain Tumor", "https://en.wikipedia.org/wiki/Brain_tumor")
    with col2:
        st.link_button("Heart Disease", "https://en.wikipedia.org/wiki/Cardiovascular_disease")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image('logo1.png',caption=None, width=400, use_column_width=450, clamp=False, channels="RGB", output_format="auto")


    


# Function to create the about us page


# You can add as many team members as you want, each with their own card
# Function to create the contact us page

# Create a sidebar for navigation
#st.sidebar.title("PrediX")

# Add a radio button for navigation
#page = st.sidebar.radio("Go to", ["Home","About Us", "Contact Us","Login"])

# Call the corresponding function based on the selected page
