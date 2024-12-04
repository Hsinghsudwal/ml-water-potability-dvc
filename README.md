# Water-Quality

## PROBLEM
In some regions having access to drinking-water is essential to health, a basic human right. With investments in water supply and sanitation can benefit economic. Since the reductions in health-care costs, which outweigh the costs of undertaking the interventions on human life. So to solve this problen can tackle with machine learning algorithms to predict if drinking water is save or not

# DATASET
[Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)

1. ph: pH of 1. water (0 to 14).
2. Hardness: Capacity of water to precipitate soap in mg/L.
3. Solids: Total dissolved solids in ppm.
4. Chloramines: Amount of Chloramines in ppm.
5. Sulfate: Amount of Sulfates dissolved in mg/L.
6. Conductivity: Electrical conductivity of water in μS/cm.
7. Organic_carbon: Amount of organic carbon in ppm.
8. Trihalomethanes: Amount of Trihalomethanes in μg/L.
9. Turbidity: Measure of light emiting property of water in NTU.
10. Potability: Indicates if water is safe for human consumption. 

### Class Labels
Potable -1 and Not potable -0

## Local setup
**Installation:** Clone the repository `git clone https://github.com/Hsinghsudwal/ml-water-quality.git`

1. Set up Environment for managing libraries and running python scripts.
    install pipenv via cmd terminal if isn't install on your machine.
   ```bash
   pip install pipenv
   ```
2. **Activate environment**
   ```bash
   pipenv shell 
   ```
   This will create pipfile and pipfilelock within the environment.

3. **Initialize a New Pipenv Environment and Install Dependencies**:
   ```bash
   pipenv install 
   ```
   `pipenv install -r requirements.txt`

## Notebook
**Run Jupyter Notebook**:
From your main project directory on terminal within Pipenv virtual environment, `cd notebook`

```bash
   jupyter lab
   ```
Perform EDA, Feature Engineering, Model Trainer and Model Evaluation.

## SRC
This directory contains two folder.
1. In `step` contains python scriptes for `data_ingestion`, `data_transformation`, `model_trainer`, and `model_evaluation`.

2. In utility contains utils file.

within the pipenv virtual environment, you can run it from your main project directory:  
   ```bash
   python main.py
   ```
This script will output the `raw.csv`, `transform.csv`, `model.joblib` and `model evaluation metric` file to save into `output` folder and use in deployment.

## Deployment
**Docker and Flask**:

1. Flask
2. test api
3. Docker: build, run
4. Api

## Cloud
* deploy on cloud

## Monitor
* Model Performance
* Data Drift




