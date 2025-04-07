import sys
from src.cloud_storage.aws_storage import SimpleStorageService
from src.logger import log
from src.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact
from src.entity.config_entity import ModelPusherConfig
from src.entity.s3_estimator import Proj1Estimator

class ModelPusher: 
    def __init__(self, 
                 model_evaluation_artifact: ModelEvaluationArtifact, 
                 model_pusher_config:ModelPusherConfig):
        """ 
        :param model_evaluation_artifact: Output referece of data evaluation artifact stage. 
        :param model_pusher_config: Configuration for model pusher
        """
        self.s3=SimpleStorageService()
        self.model_evaluation_artifact=model_evaluation_artifact
        self.model_pusher_config=model_pusher_config

        self.proj1_estimator= Proj1Estimator(bucket_name=model_pusher_config.bucket_name,
                       model_path=model_pusher_config.s3_model_key_path)
        
    def initiate_model_pusher(self)->ModelPusherArtifact: 
        """ 
        Mehtod Name: inititate model evaluation
        Descripation: This function is used to initiate all steps of the model pusher.

        Output: returns model evaluation artifact
        """
        try: 
            print("-------------------------------------------------------------")
            log.info(f"Uploading artifacts folder to s3 bucket")

            log.info(f"Uploading new model to S3 bucket")
            self.proj1_estimator.save_model(from_file=self.model_evaluation_artifact.trained_model_path)
            model_push_artifact=ModelPusherArtifact(bucket_name=self.model_pusher_config.bucket_name,
                                s3_model_path=self.model_pusher_config.s3_model_key_path)
            log.info(f"Uploaded artifact folder to s3 bucket")
            log.info(f"Model Pusher artifact: {model_push_artifact}")
            log.info(f"Exited initiate model pusher method of ModelTriner class")

            return model_push_artifact
        except Exception as e: 
                raise e
        