import pandas as pd
from src.utility import *
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

class DataTransformation:
    def __init__(self):
        pass
    
    def pipeline_process(self, train,test):
        try:
            all_features=train.columns
            numerical_features = train.select_dtypes(include=['int64', 'float64']).columns.tolist()

            numerical_transformer = Pipeline(steps=[

                ('imputer', SimpleImputer(strategy='mean')), 
                ('scaler', MinMaxScaler())  
                ])
            preprocessor = ColumnTransformer(
                transformers=[('num', numerical_transformer, numerical_features)]
                )
            df_train_preprocessed = preprocessor.fit_transform(train)
            df_test_preprocessed = preprocessor.fit_transform(test)

            df_preprocess_train = pd.DataFrame(df_train_preprocessed, columns=all_features)
            df_preprocess_test = pd.DataFrame(df_test_preprocessed, columns=all_features)

            return df_preprocess_train, df_preprocess_test
        
        except Exception as e:
            raise Exception(e)
        
    def dataTransform(self, train_path,test_path):
        try:
            # data Transform
        
            df_preprocess_train, df_preprocess_test=DataTransformation.pipeline_process(self,train_path,test_path)

            # create path to store processor data
            df_preprocess_train.to_csv(os.path.join('output',str('process_train_data.csv')))
            df_preprocess_test.to_csv(os.path.join('output',str('process_test_data.csv')))
            print('Data Transformation Completed')
            return df_preprocess_train, df_preprocess_test

        except Exception as e:
            raise Exception(e)
