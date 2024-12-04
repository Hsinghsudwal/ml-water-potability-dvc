import os
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class Utility:
    def __init__(self) -> None:
        pass

    def create_folder(folder_name):
        try:
            # Creating a directory if it does not exist already
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

        except Exception as e:
            raise e
        
    def read_data(data):
        try:
            # read dataframe
            df = pd.read_csv(data)
            return df

        except Exception as e:
            raise e
        
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
            raise e
        
    def metrics_score(y_test, y_pred):
        try:

            accuracy = round(accuracy_score(y_test, y_pred),2)
            precision = round(precision_score(y_test, y_pred),2)
            recall = round(recall_score(y_test, y_pred),2)
            f1 = round(f1_score(y_test, y_pred),2)
        
            return accuracy,precision,recall,f1
        
        except Exception as e:
            raise e