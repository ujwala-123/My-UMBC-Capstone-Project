# Content
## Capstone Project Spring 2023
## Maryland Statewide Vehicle Crashes - predicting severity of injury 
The data we will be working with is the Maryland Statewide Vehicle crashes dataset taken from https://opendata.maryland.gov/. This dataset consists of crashes that occured in the Maryland state from 2015 to 2022. This dataset has three sub-datasets which are:

Dataset-1: Maryland Statewide Vehicle Crashes:
https://opendata.maryland.gov/Public-Safety/Maryland-Statewide-Vehicle-Crashes/65du-s3qu

Dataset-2: Person Details:
https://opendata.maryland.gov/Public-Safety/Maryland-Statewide-Vehicle-Crashes-Person-Details-/py4c-dicf

Dataset-3: Vehicle Details:
https://opendata.maryland.gov/Public-Safety/Maryland-Statewide-Vehicle-Crashes-Vehicle-Details/mhft-5t5y

After merging the given datasets with common column REPORT_NO, the columns of the final dataframe and their types are:\
ACC_DATE            int64\
ACC_TIME           object\
WEATHER_DESC       object\
REPORT_NO          object\
COUNTY_DESC        object\
LATITUDE          float64\
LONGITUDE         float64\
SURF_COND_DESC     object\
RD_COND_DESC       object\
RD_DIV_DESC        object\
SEX_DESC           object\
DATE_OF_BIRTH      object\
INJ_SEVER_DESC     object\
VEH_YEAR          float64\
VEH_MAKE           object\
SPEED_LIMIT         int64\
YEAR                int64\
Quarter            object

In this dataset, the crashes data is taken vaious counties in Maryland such as "Prince George's", 'Worcester', 'Montgomery', 'Frederick', 'Calvert', 'Baltimore', 'Baltimore City', 'Washington', 'Howard','Carroll', 'Harford', 'Charles', 'Anne Arundel', 'Somerset', "St. Mary's", 'Dorchester', 'Garrett', "Queen Anne's", 'Kent','Wicomico', 'Caroline', 'Allegany', 'Cecil', 'Talbot'. 

### Problem Statement
Predicting the severity of the injury after the accident: This project aims to develop a machine-learning model that predicts the severity of injuries sustained by individuals involved in vehicle crashes in Maryland. Predicting the severity by the deployment of the model.

### Cleaning and Preprocessing using Python
1. Used Jupyter Notebook for Cleaning and Preprocessing.
2. The vehicles and persons datasets are merged on ‘VEHICLE_ID’.
3. The obtained dataset and crashes dataset are merged on ‘REPORT_NO’.
4. After preprocessing, the shape of the dataset is (619031, 22).

### Data Visualization using Tableau
1. Visualized data using Tableau.
2. Link for my Tableau public account is https://public.tableau.com/app/profile/ujwala.namineni1131 
3. The frequency of accidents is influenced by various factors such as road surface conditions, weather conditions, county, and road division type. 

### Created Machine learning model using Microsoft Azure
Created machine learning models using machine learning algorithms like multi-class Logistic Regression, Decision Tree, Boosted Decision Tree, and Random Forest. The accuracy of the best model is 80.2% in logistic regression. 
The obtained metrics are:
Macro_Precision - 0.3648
Macro_Recall - 0.2316
Micro_Precision - 0.8025
Micro_Recall - 0.8025
Overall_Accuracy - 0.8025

### Deployment using Streamlit
1. Developed a web application using Streamlit and Python.
2. Implemented a web page via the 'app.py' file and model is scripted in 'ml_model.py' file.
3. Integrated the machine learning model into the web page.
4. Defined a function to predict whether a person is injured or not.

##### PPT Link
https://docs.google.com/presentation/d/17EJoGi5BQColZlH2-Ey9Z-YTdrFXzi4u/edit?usp=share_link&ouid=102656629508192105676&rtpof=true&sd=true 

##### Youtube Link
https://youtu.be/iIKE01TZOtI


