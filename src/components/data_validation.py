import os,sys
import pandas as pd
from src.constant import SCHEMA_FILE_PATH
from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from src.utils.utils_file import read_yaml_file
from src.logger import log
from pandas import DataFrame
import json

class DataValidation: 
    def __init__(self, data_validation_config=DataValidationConfig,
                  data_ingestion_artifact=DataIngestionArtifact):
        """ 
        data_ingesion_artifact: artifact related to DataIngestion like train_path, test_path. 
        data_validation_config: configuration related to data validation. 
        """
        try: 
            self.data_validation_config=data_validation_config
            self.data_ingestion_config=data_ingestion_artifact
            self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e: 
            raise e
        
    def validate_number_of_columns(self, dataframe: DataFrame)->bool: 
        """ 
        Method Name: Validate number of columns
        Description: This method validates the number of columns

        Output: Returns bool value based on validation results. 
        """
        try: 
            status=len(dataframe.columns) == len(self._schema_config['columns'])
            log.info(f"Is requirement columns present: {status}")
            return status
        except Exception as e:
            raise e
        
    def is_columns_exist(self, df:DataFrame)->bool: 
        """ 
        Method Name: is columns exist
        Description: This method validates the existence of a numberical and cateforical columns

        output : Return bool value based on validation results. 
        """
        try:
            dataframe_columns=df.columns
            missing_numerical_name=[]
            missing_cate_name=[]

            for col in self._schema_config['numerical_columns']: 
                if col not in dataframe_columns: 
                    missing_numerical_name.append(col)
            
            if len(missing_numerical_name)>0: 
                log.info(f"Missing Numberical column: {missing_numerical_name}")

            for col in self._schema_config['categorical_columns']:
                if col not in dataframe_columns:
                    missing_cate_name.append(col)

            if len(missing_cate_name)>0:
                log.info(f"Missing categorical col: {missing_cate_name}")

            return False if len(missing_numerical_name)>0 or len(missing_numerical_name)>0 else True

        except Exception as e:
            raise e
        

    @staticmethod   
    def read_data(file_path)->DataFrame:
        try: 
            return pd.read_csv(file_path)
        except Exception as e: 
            raise e
    
    def initiate_data_validation(self)->DataValidationArtifact:
        """ 
        Method Name: Inititate data validation
        Description: This method initiate the data validation component for the pipeline

        Output: Returns bool value based on validation results.
        """
        try: 
            validation_error_msg=""
            
            log.info("Starting data Validation")
            train_df, test_df=(DataValidation.read_data(file_path=self.data_ingestion_config.trained_file_path),
                               DataValidation.read_data(file_path=self.data_ingestion_config.test_file_path))
            
            # Checking col len of dataframe for train/test df
            status=self.validate_number_of_columns(dataframe=train_df)

            if not status: 
                validation_error_msg=validation_error_msg + f"Columns are missing in training dataframe"
            else: 
                log.info(f"All requried columns are present in training dataframe: {status}")

            status=self.validate_number_of_columns(dataframe=test_df)
            if not status: 
                validation_error_msg=validation_error_msg + f"columns are missing in test dataframe"
            else: 
                log.info(f"All requriement columns present in testing dataframe: {status}")

            # validating the col in train dataframe. 
            status=self.is_columns_exist(df=train_df)
            if not status: 
                validation_error_msg=validation_error_msg+f"Columns are missing from train_df" 
            else: 
                log.info(f"All column are present in train dataframe as expected: {status}")
            
            # validating the col in test dataframe. 
            status=self.is_columns_exist(df=test_df)
            if not status: 
                validation_error_msg=validation_error_msg+ f"Columns are missing from test_df"
            else: 
                log.info(f"Column are present in test dataframe as expected: {status}")  

            validation_status=len(validation_error_msg)==0

            data_validation_artifact=DataValidationArtifact(
            validation_status=validation_status,
            message=validation_error_msg,
            validation_report_file_path=self.data_validation_config.data_validation_report_file_path
            )


            # Ensure the directory for validation report file path exits
            report_dir=os.path.dirname(self.data_validation_config.data_validation_report_file_path)
            os.makedirs(report_dir, exist_ok=True)

            # Save validation status and message to a json file
            validation_report={
                "validation_status": validation_status, 
                "message": validation_error_msg
            }
            with open(self.data_validation_config.data_validation_report_file_path, 'w') as report_file: 
                json.dump(validation_report, report_file)
            
            log.info(f"Data validation artifact created and saved to JASON file.")
            log.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        
        except Exception as e: 
            raise e




        