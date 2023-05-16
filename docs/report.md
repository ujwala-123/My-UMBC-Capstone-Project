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

![Screenshot (178)](https://github.com/ujwala-123/Ujwala_Data606/assets/72090397/3f1f18a8-d8ef-481c-81bb-814a35ced72d)

From the visualizations, 
1. In Maryland, vehicle collisions are influenced by road surface types, with more occurring on Dry and Wet roads.
2. Clear, Rainy, and cloudy weather conditions contribute to a more number of accidents in Maryland.
3. Counties such as Anne Arundel, Baltimore, Baltimore City, Montgomery, and Prince George's have a greater crash rate.
4. For every kind of injury severity, the gender distribution is almost the same.
5. The average age, accident quarter, and speed limit have little to no effect on the severity or frequency of vehicle crashes.

### Created Machine learning model using Microsoft Azure
In this project, created machine learning models using Azure Machine Learning model Studio, including multi-class Logistic Regression, Decision Tree, Boosted Decision Tree, and Random Forest, were used to develop machine learning models. 
For example,
The Boosted Decision Tree algorithm has accuracy of 77.60%.
The obtained metrics are:\
Macro_Precision - 0.2743\
Macro_Recall - 0.2138\
Micro_Precision - 0.7760\
Micro_Recall - 0.7760\
Overall_Accuracy - 0.7760

![Screenshot (160)](https://github.com/ujwala-123/Ujwala_Data606/assets/72090397/17010273-bb2e-48b2-ac0c-0777b8f9dce8)


The logistic regression model obtained the highest accuracy of 80.2% among these models.
The obtained metrics are:\
Macro_Precision - 0.3648\
Macro_Recall - 0.2316\
Micro_Precision - 0.8025\
Micro_Recall - 0.8025\
Overall_Accuracy - 0.8025

![Screenshot (158)](https://github.com/ujwala-123/Ujwala_Data606/assets/72090397/4d5ffd4a-2315-4b90-a05e-2800118d61ae)


These metrics provide valuable insight into the performance of the model in predicting the severity of injuries sustained in vehicle crashes. The high accuracy of the logistic regression model suggests that it possesses promising predictive capabilities. To obtain a comprehensive understanding of the model's performance across various classes and as a whole, it is essential to consider evaluation metrics, such as precision, recall, and accuracy.

### Deployment using Streamlit
The project required the deploying of a web application using Streamlit and Python, with a web page implemented in the 'app.py' file and a machine learning model scripted in the 'ml_model.py' file attached in 'src'. The integration of the machine learning model into the website enabled a prediction of the severity of injuries sustained in vehicle crashes.

### Conclusion
In conclusion, the analysis of the Maryland Statewide Vehicle Crashes dataset reveals that road surface types, weather conditions, and particular counties have significant effects on the occurrence and frequency of vehicle collisions in Maryland. Variables such as average age, accident quarter, and speed limit have a negligible to nonexistent effect on the severity or frequency of vehicle collisions, whereas the distribution of injuries by gender remains constant across all levels of severity. 

Developed machine learning models, especially logistic regression model with 80.2% accuracy, have significant potential for incorporation into a web application. Users can take advantage of the web app's prediction skills to determine the severity of injuries sustained in vehicle crashes by integrating the trained model into the app's backend.

Thereby, these insights can inform targeted interventions and policies designed to reduce accidents and through web app, people enhance their knowledge of the potential severity of injuries resulting from vehicle crashes in Maryland.

### Future Scope
1. Building a machine learning model with more accuracy by tuning hyperparameters.
2. Developing web application using Azure web services for more scalability, reliability and ability to integrate with other Azure services.
3. Developing a mobile application for real-time prediction and alerts.

