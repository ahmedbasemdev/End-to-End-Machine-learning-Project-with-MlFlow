from MlProject.config.configuration import ConfigurationManager
from MlProject.components.model_evaluation import ModelEvaluation
from MlProject import logger
import os 

class ModelEvaluationPipeline:
    def __init__(self):
        os.environ['MLFLOW_TRACKING_URI']='https://dagshub.com/ahmedbasemdev/End-to-End-MlOps-Project-with-MlFlow.mlflow'
        os.environ['MLFLOW_TRACKING_USERNAME']='ahmedbasemdev'
        os.environ['MLFLOW_TRACKING_PASSWORD']='b9c0edb3ac476430231e5a54f8cc5c6423e1073f'

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()

STAGE_NAME = "Model Evaluation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        raise e
