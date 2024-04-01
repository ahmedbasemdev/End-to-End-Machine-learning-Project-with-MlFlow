from MlProject import logger
from MlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MlProject.pipeline.stage_02_data_validation import DataValidationPipeLine
from MlProject.pipeline.stage_03_data_transformation import DataTranformationPipeLine



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    pipe = DataIngestionTrainingPipeline()
    pipe.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<< \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    obj = DataValidationPipeLine()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<< \n\n x==========x")
except Exception as e:
    raise e

STAGE_NAME = "Data Tranformation Stage"

try:
     logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
     obj = DataTranformationPipeLine()
     obj.main()
     logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<< \n\n x==========x")
except Exception as e:
     raise e