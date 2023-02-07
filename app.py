# Importing the important libraries
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import pickle

# with st.sidebar:
selected = option_menu(
    menu_title=None,  
    options=["Home", "Credit Scoring", "About"],
    #icons = ["Home","box","filetype-xlsx","Info"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",)

if selected == "Home":
    st.title("Home")

    # load the save model
    loaded_model  = pickle.load(open('trained_model.sav', 'rb'))

    # create a function to predict the output

    def predictor(input_data):
        #input_data = (0.00632,18.0,2.31,0.0,0.538,6.575,65.2,4.0900,1.0,296.0,15.3,396.90,4.98)
        #change the input data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)
        #reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        #prediction
        prediction = loaded_model.predict(input_data_reshaped)
        return prediction

    def main():
        # giving a title to the web app
        st.title("Salary Predictor")
        # getting the input from the user
        #YearsExperience = st.text_input("YearsExperience")
        # getting input number from the user
        YearsExperience = st.number_input("YearsExperience")
        # code for prediction
        diagnosis = ''
        if st.button("Predict"):
            diagnosis = predictor([YearsExperience])
            st.success('The salary is {}'.format(diagnosis))

    if __name__ == '__main__':
        main()




elif selected == "Credit Scoring":
    st.title("Credit Scoring")
elif selected == "About":
    st.title("About")
else :
    st.title("Error 404")

