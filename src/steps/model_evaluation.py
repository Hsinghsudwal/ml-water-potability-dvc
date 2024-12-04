import json
import joblib
from src.utility import *

import os


class ModelEvaluation:
    def __init__(self):
        pass

    def modelEvaluation(self, preprocess_train, preprocess_test):
        try:
        #    modelevaluation
           x_test = preprocess_test.drop(columns=['Potability'], axis=1).values
           y_test = preprocess_test['Potability'].values

           model_path=os.path.join('output',str('best_model.joblib'))
           model=joblib.load(model_path,"r")
           ypred=model.predict(x_test)

           accuracy,precision,recall,f1=Utility.metrics_score(y_test,ypred)

           metric_dic={'accuracy':accuracy,
                       'precision':precision,
                       'recall':recall,
                       'f1':f1
                       }
           print(metric_dic)
           metric_file=os.path.join('output',str('model_eval_metrics.json'))
           
           with open(metric_file,'w') as f_in:
            json.dump(metric_dic,f_in,indent=4)
           
           print('Model Evaluation Completed')

        except Exception as e:
            raise Exception(e)