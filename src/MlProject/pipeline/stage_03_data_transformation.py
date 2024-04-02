from MlProject.config.configuration import ConfigurationManager
from MlProject.components.data_transformation import DataTransformation
from MlProject import logger
from pathlib import Path
import os

class DataTranformationPipeLine:
    def __init__(self) -> None:
        logger.info(os.curdir)
        pass

    def main(self):
            try:
                with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                      status = f.read().split(" ")[-1]
                if status == "True":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(data_transformation_config)
                    data_transformation.train_test_spliting()
                else:
                     raise Exception(" Your Data Schema is not valid")
            except Exception as e:
                 raise e

STAGE_NAME = "Data Tranformation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} Started <<<<<<")
        obj = DataTranformationPipeLine()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        raise e