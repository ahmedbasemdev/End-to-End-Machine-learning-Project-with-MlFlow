from MlProject.config.configuration import ConfigurationManager
from MlProject.components.data_transformation import DataTransformation
from MlProject import logger

class DataTranformationPipeLine:
    def __init__(self) -> None:
        pass

    def main(self):
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.train_test_spliting()

STAGE_NAME = "Data Tranformation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        obj = DataTranformationPipeLine()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        raise e