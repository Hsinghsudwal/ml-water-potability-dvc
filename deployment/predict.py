import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify

model = joblib.load(open('.output/best_model.joblib','rb'))

app = Flask('Cirrhosis')

@app.route('/predict', methods=['POST'])
def predict():
    sample = request.get_json()
   
    x=pd.DataFrame([sample])

    x = StandardScaler().transform(x)

    test=x.values.reshape(1, -1)

    prediction = model.predict(test)[0]
    
    status=None
    if prediction == 1:
        status = "Potable"

    else:
        status = "Not potable"
    
    result={
        int(prediction):(status)
    }
    
    return jsonify([result])

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 9696)