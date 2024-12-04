import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.utility import *

import os

class DataIngestion:
    def __init__(self):
        pass

    def dataIngestion(self, path):
        try:
            # read data
            data=Utility.read_data(path)
            print(data.head())
            # split into train test
            train_data, test_data = train_test_split(data, test_size= 0.20, random_state=42)
            # create folder to store data
            Utility.create_folder('output')
            os.makedirs('output',exist_ok=True)
            # save train test to csv
            train_data.to_csv(os.path.join('output',str('raw_train_data.csv')))
            test_data.to_csv(os.path.join('output',str('raw_test_data.csv')))
            print('Raw Data Completed')
            return train_data, test_data

        except Exception as e:
            raise Exception(e)