# Content
## Capstone Project Spring 2023
## Maryland Statewide Vehicle Crashes - predicting severity of injury 
##### PPT Link
https://docs.google.com/presentation/d/17EJoGi5BQColZlH2-Ey9Z-YTdrFXzi4u/edit?usp=share_link&ouid=102656629508192105676&rtpof=true&sd=true 
##### Youtube Link
https://youtu.be/iIKE01TZOtI

### Introduction
The Maryland Statewide Vehicle Crashes dataset, retrieved from https://opendata.maryland.gov/, contains a comprehensive compilation of data on vehicle collisions that occurred in Maryland between 2015 and 2022. This extensive dataset consists of three sub-datasets and provides valuable insights into the causes, locations, and characteristics of these incidents. By analyzing the dataset, I aim to identify patterns, correlations, and risk factors associated with collisions, thereby laying the groundwork for evidence-based decision-making, targeted interventions, and policy recommendations to improve road safety and reduce accidents in Maryland.

### Problem Statement
This project's objective is to create a machine-learning model capable of reliably predicting the severity of injuries sustained by individuals involved in vehicle collisions in Maryland. Predicting the severity of injuries can considerably improve emergency response planning, resource allocation, and medical interventions. Using the Maryland Statewide Vehicle Crashes dataset, I intend to train a model that can accurately evaluate the various factors and attributes associated with a collision and classify the severity of injuries. This predictive model can provide valuable insights to decision-makers, emergency services, and healthcare providers, allowing them to efficiently prioritize and allocate resources, ultimately resulting in improved medical outcomes and increased road safety in Maryland.

Finally, the major problems need to be solved are:
1. What are the main factors contributing to vehicle crashes in Maryland, according to the Maryland Statewide Vehicle Crashes dataset?
2. How accurately can a machine-learning model predict the severity of injuries sustained in vehicle crashes using the Maryland Statewide Vehicle Crashes dataset?

### Datasets
The three datasets taken are:\
Dataset-1: Maryland Statewide Vehicle Crashes:
https://opendata.maryland.gov/Public-Safety/Maryland-Statewide-Vehicle-Crashes/65du-s3qu
Dataset-2: Person Details:
https://opendata.maryland.gov/Public-Safety/Maryland-Statewide-Vehicle-Crashes-Person-Details-/py4c-dicf
Dataset-3: Vehicle Details:
https://opendata.maryland.gov/Public-Safety/Maryland-Statewide-Vehicle-Crashes-Vehicle-Details/mhft-5t5y

After merging the given datasets with common column REPORT_NO and VEHICLE_ID, the columns of the final dataframe and their types are:\
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

In this dataset, the crashes data is taken vaious counties in Maryland such as 'Prince George's', 'Worcester', 'Montgomery', 'Frederick', 'Calvert', 'Baltimore', 'Baltimore City', 'Washington', 'Howard','Carroll', 'Harford', 'Charles', 'Anne Arundel', 'Somerset', "St. Mary's", 'Dorchester', 'Garrett', "Queen Anne's", 'Kent','Wicomico', 'Caroline', 'Allegany', 'Cecil', 'Talbot'. 

### Cleaning and Preprocessing using Python
The following steps were performed during the cleaning and preprocessing phase of this project to ensure the quality and usability of the Maryland Statewide Vehicle Crashes dataset:
1. Missing data: Columns with missing data were identified and incomplete records were removed.
2. Merging Datasets: 
    a) The vehicles and persons datasets were merged based on the shared identifier 'VEHICLE_ID' in order to consolidate information regarding the vehicles involved and the        individuals affected by the accidents.
    b) The dataset resulting from the previous phase was then merged with the crashes dataset using the common identifier 'REPORT_NO' to create a comprehensive dataset            containing information about the crashes, vehicles, and individuals involved.
3. After cleaning and preprocessing, the final form of dataset consists of 619,031 records and 22 features and has the shape (619031, 22).

### Data Visualization using Tableau
During the analysis phase, Tableau, a powerful data visualization tool, was used to visualize the data. Accessible at https://public.tableau.com/app/profile/ujwala.namineni1131 is the project's Tableau public account, which features interactive visualizations of insights and patterns discovered in the Maryland Statewide Vehicle Crashes dataset.

The dashboards of the visualizations are:
![Screenshot (177)](https://github.com/ujwala-123/Ujwala_Data606/assets/72090397/df8a8cb3-59e6-4732-b288-f4234f2c0978)


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
