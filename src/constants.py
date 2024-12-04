# BASE:
PROJECT_NAME = "Water Quality"
AUTHOR = "Harinder Singh Sudwal"

# Data Ingestion
TEST_SIZE = 0.2
OUTPUT='output'
RAW_FOLDER='raw'
TRAIN_DATA_FILE='train_data.csv'
TEST_DATA_FILE='test_data.csv'

# Data Validation
THRESHOLD=0.05
VALIDATE_FOLDER='validate'
REPORT_VALIDATE_JSON='report.json'

# Data Transformer
TRANSFORMATION_FOLDER='transformation'
TRAIN_PROCESS_DATA_FILE='train_process.csv'
TEST_PROCESS_DATA_FILE='test_process.csv'

# Model Trainer
BEST_MODEL=0.65
MODEL_FOLDER='model'
BEST_MODEL_NAME='best_model.joblib'
MODELS_FILE='model.csv'

# Model Evaluation
EVALUATION_FOLDER='evaluate'
EVAL_JSON_NAME='model_eval_metrics.json'
