import pandas as pd
import numpy as np
import json
import joblib
from src.utility import *
import os
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


class ModelTrainer:
    
    def __init__(self):
        pass
    
    def models_list(self):

        try:
           
           models={
               'gbc':GradientBoostingClassifier(),
               'tree':DecisionTreeClassifier(),
               'random_forest':RandomForestClassifier(),
               'linear_model': LogisticRegression(),
               'svm': LinearSVC(),
               'naive_bayes':GaussianNB(),
               'k-neighbor':KNeighborsClassifier(),
            }
           
           return models
           
        except Exception as e:
            raise Exception(e)

    def best_model(self, preprocess_train, preprocess_test):
        try:
           x_train = preprocess_train.drop(columns=['Potability'], axis=1).values
           y_train = preprocess_train['Potability'].values

           x_test = preprocess_test.drop(columns=['Potability'], axis=1).values
           y_test = preprocess_test['Potability'].values

           models =ModelTrainer.models_list(self)

           for name, model in models.items():
               model.fit(x_train, y_train)
               y_pred = model.predict(x_test)
               acc_test = accuracy_score(y_test, y_pred)
            #    print(name, model, acc_test)             

               if acc_test > 0.60:
                #    print(name, model)
                   return model
               else:
                   print("Error - model perform below best score")
                   
               return model
        
        except Exception as e:
            raise Exception(e)
        
    def modelTrainer(self, preprocess_train, preprocess_test):
        try:
           # modele
           x_train = preprocess_train.drop(columns=['Potability'], axis=1).values
           y_train = preprocess_train['Potability'].values

           x_test = preprocess_test.drop(columns=['Potability'], axis=1).values
           y_test = preprocess_test['Potability'].values

           best_model=ModelTrainer.best_model(self, preprocess_train, preprocess_test)
           
           best_model.fit(x_train, y_train)
           print('best model train score: ', best_model.score(x_train, y_train))

         #   create path to store model
           modelfilepath=os.path.join('output',str('best_model.joblib'))
           model_file=joblib.dump(best_model, modelfilepath)
           print('Model Trainer Completed')

           return model_file

        except Exception as e:
            raise Exception(e)

    
