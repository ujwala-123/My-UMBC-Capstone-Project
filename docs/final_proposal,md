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

## Goal: My goal is to predict whether the person is severely injured or not/with minor injuries.
Here, I am categorizing No Injury, Non-incapacitating Injury as minorly injured and Incapacitating/Disabled Injury, Possible Incapacitating Injury, Non-incapacitating Injury, Fatal Injury as severely injured.
Features to predict this are: Weather, which quater of the year, road surface conditions, road type, etc.,

Through this prediction we can find major reason or reasons for serious injuries or death and eventually do some changes.

## ML models
I am planning to use different classification machine learning models like logistic regression, decision tree, random forest, etc.,
I will compare them with the accuracy of each model.

## Deployment
Creating a simple web application that will generate whether the person minorly injured or severely injured from the given features.
