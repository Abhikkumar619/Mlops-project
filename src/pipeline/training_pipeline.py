import sys
from  src.logger import log
from src.components.data_ingestion import DataIngestion

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline: 
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def start_data_ingestion(self)->DataIngestionArtifact: 
        """ 
        This method of TrainPipeline class is responsiable for starting data ingestion component
        """
        try: 
            log.info("Entred the start_data_ingestion method of TrainPipeline class")
            log.info("Getting the data from Mongodb")

            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_intestion()
            log.info("Got the train set and test set from mongodb")
            log.info("Exited the start data ingestion method of Trainpipeline class")
            log.info("Exited the start data ingestion method of trainPipeline class")
            return data_ingestion_artifact

        except Exception as e: 
            raise e


    def run_pipeline(self)->None: 
        """ 
        This method of TrainPipeline class is responsible for running complete pipeline.
        """
        try: 
            data_ingestion_artifact=self.start_data_ingestion()
            
        except Exception as e: 
            raise e