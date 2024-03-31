from MlProject import logger
from MlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    pipe = DataIngestionTrainingPipeline()
    pipe.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e