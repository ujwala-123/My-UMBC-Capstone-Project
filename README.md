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

### Cleaning and Preprocessing using Python
### Data Visualization using Tableau
### Created Machine learning model using Microsoft Azure

## Visualization
From visualizations, we can conclude that,
Most accidents are happend
1. In 4,5,6 quater in a day.
2. if the surface of road is Dry and then Wet.
3. if weather condition is
## ML models
Created machine learning models using machine learning algorithms like multi-class Logistic Regression, Decision tree, Boosted Decision Tree. The accuracy of best model is 80.2% in logistic regression. 
The obtained metrics are:
Macro_Precision - 0.3648
Macro_Recall - 0.2316
Micro_Precision - 0.8025
Micro_Recall - 0.8025
Overall_Accuracy - 0.8025

