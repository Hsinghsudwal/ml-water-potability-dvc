import os
import pandas as pd

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
        
    def metrics_score(y_test, y_pred):
        try:

            accuracy = round(accuracy_score(y_test, y_pred),2)
            precision = round(precision_score(y_test, y_pred),2)
            recall = round(recall_score(y_test, y_pred),2)
            f1 = round(f1_score(y_test, y_pred),2)
        
            return accuracy,precision,recall,f1
        
        except Exception as e:
            raise e