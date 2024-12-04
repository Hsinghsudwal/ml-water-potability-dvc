from src.steps.data_ingestion import DataIngestion
from src.steps.data_transformation import DataTransformation
from src.steps.model_trainer import ModelTrainer
from src.steps.model_evaluation import ModelEvaluation

def main():
    try:
        path=r"data/water_quality.csv"
        # file=r"output/model/model_gbc.joblib"
        data_ingest=DataIngestion()
        train_data,test_data=data_ingest.dataIngestion(path)

        preprocess=DataTransformation()
        preprocess_train, preprocess_test=preprocess.dataTransform(train_data,test_data)

        model_trainer=ModelTrainer()
        model_trainer.modelTrainer(preprocess_train, preprocess_test)

        model_evaluate=ModelEvaluation()
        model_evaluate.modelEvaluation(preprocess_train, preprocess_test)
        # if retrain:

    except Exception as e:
        raise Exception(e)
    


if __name__=="__main__":
    main()
