import pandas as pd
from src.utility import *
import os

class DataTransformation:
    def __init__(self):
        pass
    
        
    def dataTransform(self, train_path,test_path):
        try:
            # data Transform
        
            df_preprocess_train, df_preprocess_test=Utility.pipeline_process(self,train_path,test_path)

            # create path to store processor data
            df_preprocess_train.to_csv(os.path.join('output',str('process_train_data.csv')))
            df_preprocess_test.to_csv(os.path.join('output',str('process_test_data.csv')))
            print('Data Transformation Completed')
            return df_preprocess_train, df_preprocess_test

        except Exception as e:
            raise Exception(e)
