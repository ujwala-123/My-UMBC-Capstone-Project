import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.cm as cm
from statsmodels.stats.weightstats import ztest


crashes = pd.read_csv('Maryland_Statewide_Vehicle_Crashes.csv',low_memory=False)
vehicles = pd.read_csv('Maryland_Statewide_Vehicle_Crashes_-_Vehicle_Details.csv',low_memory=False)
persons = pd.read_csv('Maryland_Statewide_Vehicle_Crashes_-_Person_Details__Anonymized_.csv',low_memory=False)

crashes_df=crashes[['ACC_DATE', 'ACC_TIME','WEATHER_DESC','REPORT_NO','COUNTY_DESC','LATITUDE', 'LONGITUDE','SURF_COND_DESC', 'RD_COND_DESC',
       'RD_DIV_DESC']]
persons_df=persons[['REPORT_NO','SEX_DESC','DATE_OF_BIRTH','INJ_SEVER_DESC', 'PERSON_TYPE_DESC', 'VEHICLE_ID']]
vehicles_df=vehicles[['VEH_YEAR', 'VEH_MAKE','SPEED_LIMIT','YEAR','Quarter', 'VEHICLE_ID']]

persons_df.drop(persons_df[persons_df['VEHICLE_ID'] == 'Pedestrian'].index, inplace = True)
data = pd.merge(vehicles_df,persons_df,on = 'VEHICLE_ID')
final_data = pd.merge(data,crashes_df,on = 'REPORT_NO')
final_data.PERSON_TYPE_DESC.unique()
final_data.INJ_SEVER_DESC.unique()


final_data['DATE_OF_BIRTH']=pd.to_datetime(final_data['DATE_OF_BIRTH'], errors='coerce')
final_data['DOB_YEAR'] = final_data['DATE_OF_BIRTH'].dt.year
final_data['AGE']=2023-final_data['DOB_YEAR']
final_data['accident_date']=pd.to_datetime(final_data['ACC_DATE'],format='%Y%m%d')
final_data['accident_datetime']=pd.to_datetime(final_data['accident_date'].astype(str)+' '+final_data['ACC_TIME'].astype(str))
final_data=final_data.dropna()
final_data=final_data[final_data['SPEED_LIMIT']>0]
final_data=final_data[(final_data.WEATHER_DESC != 'Not Applicable') \
                                  & (final_data.WEATHER_DESC != 'Unknown') \
                                  & (final_data.WEATHER_DESC != 'Other') \
                                  & (final_data.WEATHER_DESC != 'null')]
final_data=final_data[(final_data.RD_COND_DESC != 'Not Applicable')]
final_data=final_data[(final_data.SURF_COND_DESC != 'Not Applicable')]
final_data=final_data[(final_data.AGE > 0)]
final_data.drop(['ACC_DATE','ACC_TIME'], axis = 1, inplace=True)
final_data['VEH_YEAR'] = final_data['VEH_YEAR'].astype(int)
final_data['DOB_YEAR'] = final_data['DOB_YEAR'].astype(int)
final_data['AGE'] = final_data['AGE'].astype(int)
final_data['DATE_OF_BIRTH'] = pd.to_datetime(final_data['DATE_OF_BIRTH'] )  # convert the 'date' column to datetime

# convert the datetime column to float
final_data['DATE_OF_BIRTH']  = final_data['DATE_OF_BIRTH'] .apply(lambda x: x.timestamp())
final_data['accident_date'] = pd.to_datetime(final_data['accident_date'] )  # convert the 'date' column to datetime

# convert the datetime column to float
final_data['accident_date']  = final_data['accident_date'] .apply(lambda x: x.timestamp())
final_data['accident_datetime'] = pd.to_datetime(final_data['accident_datetime'] )  # convert the 'date' column to datetime

# convert the datetime column to float
final_data['accident_datetime']  = final_data['accident_datetime'] .apply(lambda x: x.timestamp())
categories = {'No Injury': 'No Injury', 'Non-incapacitating Injury': 'Injury', 
              'Possible Incapacitating Injury': 'Injury', 'Incapacitating/Disabled Injury': 'Injury', 
              'Fatal Injury': 'Injury'}

# use pandas.map() to categorize the values based on categories
final_data['INJ_SEVER_DESC'] = final_data['INJ_SEVER_DESC'].map(categories)
X = final_data[['VEH_YEAR', 'SPEED_LIMIT', 'YEAR', 'DOB_YEAR', 'AGE']]
y = final_data['INJ_SEVER_DESC']


from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
categorical_features = X.select_dtypes(include="object").columns
numerical_features = X.select_dtypes(exclude="object").columns
num_pipe = Pipeline([('impute_missing', SimpleImputer(missing_values = np.nan,strategy='mean')),
                           ('standardize_num', StandardScaler())
                        ])

cat_pipe = Pipeline([('impute_missing', SimpleImputer(missing_values = np.nan ,strategy='most_frequent')),
                          ('create_dummies', OneHotEncoder())])

processing_pipeline = ColumnTransformer(transformers=[('proc_numeric', num_pipe, numerical_features),
                                                      ('create_dummies', cat_pipe, categorical_features)
                                                     ])
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

# Create an instance of the ordinal encoder
encoder = OrdinalEncoder()

# Fit the encoder to the categorical features in X
X_encoded = encoder.fit_transform(X[categorical_features])

# Combine the encoded categorical features with the numeric features
X_processed = np.concatenate((X_encoded, X[numerical_features]), axis=1)

# Split the processed data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)
def map_target(value):
    if value == 'Injury':
        return 1
    else:
        return 0

# Apply the mapping function to the target column
final_data['INJ_SEVER_DESC'] = final_data['INJ_SEVER_DESC'].apply(map_target)
cat_pipe.fit(X_train,y_train)
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
accuracy = logreg.score(X_test, y_test)
from sklearn.metrics import classification_report

y_pred = logreg.predict(X_test)
import pickle
features = ['VEH_YEAR', 'SPEED_LIMIT', 'YEAR', 'DOB_YEAR', 'AGE']
target = 'INJ_SEVER_DESC'

with open('model.pkl', 'wb') as f:
    pickle.dump(logreg, f)

def predict_injury_severity(input_data):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    X = pd.DataFrame(input_data, index=[0])[features]
    prediction = model.predict(X)
    return prediction


