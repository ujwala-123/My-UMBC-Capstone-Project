import streamlit as st
import ml_model
import numpy as np

# create input widgets for each column
def app():
    st.set_page_config(page_title='Injury Severity Prediction', page_icon=':car:', layout='wide')
    st.title('Injury Severity Prediction')

    # create input widgets for each column
    veh_year = st.number_input('Vehicle Year', min_value=1900, max_value=2023, value=2000, step=1)
    speed_limit = st.number_input('Speed Limit', min_value=0, max_value=100, value=30, step=1)
    year = st.number_input('Year_accident', min_value=1900, max_value=2023, value=2022, step=1)
    dob_year = st.number_input('dob_year', min_value=1900, max_value=2023, value=2000, step=1)
    age = st.number_input('AGE', min_value=17, max_value=70, value=25, step=1)
    # create a button to make the prediction
    if st.button('Predict Injury Severity'):
    # get the input values from the user
        input_dict = {
        'VEH_YEAR': veh_year,
        'SPEED_LIMIT': speed_limit,
        'YEAR': year,
        'DOB_YEAR': dob_year,
        'AGE': age,
        }
    
    # make the prediction using the model
        predicted_injury_severity = ml_model.predict_injury_severity(input_dict)
    
    # show the predicted injury severity to the user
        st.write('Predicted Injury Severity:', predicted_injury_severity)
app()