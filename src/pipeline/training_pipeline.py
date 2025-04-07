import sys
from  src.logger import log

# Components
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

# Configuration 
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import DataValidationConfig
from src.entity.config_entity import DataTransformationConfig
from src.entity.config_entity import ModelTrainerConfig, ModelEvaluationConfig

# Artifacts
from src.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact
from src.entity.artifact_entity import DataValidationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact

class TrainPipeline: 
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.data_validation_config=DataValidationConfig()
        self.data_transformation_config=DataTransformationConfig()
        self.model_trainer_config=ModelTrainerConfig()
        self.model_evaluation_config=ModelEvaluationConfig()

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
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact)->DataValidationArtifact:
        """
        The method of TrainPipeline class responsible for starting data validation components
        """
        log.info(f"Entered the start validation method of TrainPipeline class")
        try: 
            data_validation=DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config)
            
            data_validation_artifact=data_validation.initiate_data_validation()

            log.info(f"Performed the data validation operation")
            log.info(f"Exited the start data validation method of TrainPipeline class")

            return data_validation_artifact
        except Exception as e:
            raise e
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            data_transformation = DataTransformation(data_ingestion_artifact=data_ingestion_artifact,
                                                     data_transformation_config=self.data_transformation_config,
                                                     data_validation_artifact=data_validation_artifact)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise e
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        """
        This method of TrainPipeline class is responsible for starting model training
        """
        try:
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                         model_trainer_config=self.model_trainer_config
                                         )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact

        except Exception as e:
            raise e
    

    def start_model_evaluation(self, data_ingestion_artifacts: DataIngestionArtifact,
                               model_trainer_artifact: ModelTrainerArtifact)-> ModelEvaluationArtifact:
        """ 
        This method of TrainPipeline class is responsiable for starting model evaluation.
        """
        try: 
            model_evaluation=ModelEvaluation( model_eval_config=self.model_evaluation_config, 
                            data_ingestion_artifact=data_ingestion_artifacts, 
                            model_trainer_artifact= model_trainer_artifact)
            
            model_evaluation_artifact=model_evaluation.initiate_model_evaluation()
            return model_evaluation_artifact
        except Exception as e: 
            raise e


    def run_pipeline(self)->None: 
        """ 
        This method of TrainPipeline class is responsible for running complete pipeline.
        """
        try: 
            # data_ingestion_artifact=self.start_data_ingestion()
            # print(f"Data Ingestion artifact from run pipeline: {data_ingestion_artifact}")
            data_ingestion_artifact= DataIngestionArtifact(trained_file_path='artifact/04_03_2025_18_30_19/data_ingestion/ingested/train.csv', test_file_path='artifact/04_03_2025_18_30_19/data_ingestion/ingested/test.csv')
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformatiom_artifact= self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
                                            data_validation_artifact=data_validation_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformatiom_artifact)
            model_evaluation_artifact= self.start_model_evaluation(
                data_ingestion_artifacts=data_ingestion_artifact, model_trainer_artifact=model_trainer_artifact)
            
            log.info(f"Model Evaluation Artifact: {model_evaluation_artifact}")

            
            
        except Exception as e: 
            raise e