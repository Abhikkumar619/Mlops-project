import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from src.entity.config_entity import DataIngestionConfig
from src.logger import log
from src.data_access.proj1_data import Proj1Data
from pandas import DataFrame
import os
from src.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config=DataIngestionConfig) ->None:
        """ 
        data_ingestion_config: configuration for data ingestion.
        """
        try: 
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise e
        
    def export_data_into_features_store(self)->DataFrame:
        """ 
        Method Name: export_data_into_features_store
        Description: This method exprots data from mongodb to csv file

        output: data is returned as artifacts of dataingestion components.

        """
        try: 
            log.info(f"Exporting data from mongodb")
            my_data=Proj1Data()
            dataframe=my_data.export_collection_as_dataframe(collection_name=
                                                             self.data_ingestion_config.collection_name)
            log.info(f"Shape of dataframe: {dataframe.shape}")
            features_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(features_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            log.info(f"Saving exported data into feature store file path: {features_store_file_path}")
            dataframe.to_csv(features_store_file_path, index=False, header=True)
            return dataframe

        except Exception as e:
            raise e
        

    def split_data_as_train_test(self,dataframe:DataFrame)->None:
        try: 
            train_set, test_set=train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ration)
            log.info("Perfored train test split on the dataframe")
            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)

            log.info("Exporting train and test file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            log.info(f'Exporting train and test file path')

        except Exception as e:
            raise e
        
    def initiate_data_intestion(self): 
        """  
        Method Name: Initiate data ingestion
        Desctiption: This method initiate the data ingestion components of training pipeline

        output: train set and test set are returned as the artifacts of data ingestion compnenets

        """
        log.info(f'Entered initiate data ingestion method of Data Ingestion class')
        try: 
            dataframe=self.export_data_into_features_store()
            log.info(f"Hot the data from mongo")

            self.split_data_as_train_test(dataframe)
            log.info("perfored train test split on the dataset")

            data_ingestion_artifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                  test_file_path=self.data_ingestion_config.testing_file_path)
            
            log.info(f"data ingestion aritfacts: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e: 
            raise e



        