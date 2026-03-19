from src.utils.common import read_yaml,create_directories
from src.constants.path import (
    PARAMS_FILE_PATH,
    SCHEMA_FILE_PATH,
    CONFIG_FILE_PATH
    )
from src.entity.config_entity import (
     DataIngestionConfig,
     DataValidationConfig,
     DataTransformationConfig,
     ModelTrainerConfig
    )

class ConfigurationManger:
    # instance variable is configfilepath , pramsfilepath and schema file path 
    def __int__(self ,
                config_path=CONFIG_FILE_PATH,
                params_path=PARAMS_FILE_PATH,
                schema_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        create_directories([self.config.data_ingestion])

    def get_data_ingestion(self) -> DataIngestionConfig:

        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config= DataIngestionConfig(
             root_dir = config.root_dir, 
             source_URL= config.source_URL,
             local_data_file = config.local_data_file,
             unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation(self) -> DataValidationConfig:

        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])

        data_ingestion_config= DataValidationConfig(

            root_dir = config.root_dir,
            data_path = config.data_path,
            status_file = config.status_file,
            all_schema = schema

        )

        return data_ingestion_config

    def get_data_transformation(self) -> DataTransformationConfig:

        config = self.config.data_transformation
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(

        )

        return data_transformation_config
    def get_model_training(self) -> ModelTrainerConfig:

        config= self.config.root_dir
        create_directories([config])
        
        model_trainer_config = ModelTrainerConfig(

        )

        return model_trainer_config





        

