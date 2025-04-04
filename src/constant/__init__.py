import os
from datetime import date
# For mongoDB connection
DB_NAME="Mlops_pro"
collection_name="vehicle"
MONGODB_URL_KEY="MON"

PIPELINE_NAME:str=""
ARTIFACT_DIR: str='artifact'

MODEL_FILE_NAME="model.pkl"


FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


# Data Ingestion related constant. 
DATA_INGESTION_COLLECTION_NAME: str = "vehicle"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25


TARGET_COLUMN = "Response"
CURRENT_YEAR = date.today().year

# Data Validation related constant. 
DATA_VALIDATION_DIR_NAME:str='data_validation'
VALIDATION_REPORT_FILE_PATH: str='report.yaml'


# Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"


PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"