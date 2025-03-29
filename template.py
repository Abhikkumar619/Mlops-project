from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s : %(message)s]")


project_name="src"


list_of_file=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils_file.py",
    "app.py",
    "requriement.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml"   
]

for path in list_of_file: 
    filepath=Path(path)
    file_dir, file_name= os.path.split(filepath)
    if file_dir !="": 
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"directory is created: {file_dir}")
    if (not os.path.exists(filepath)) or os.path.getsize(filepath==0): 
        with open(filepath, "w") as f: 
            pass
    else:
        logging.info(f"file is already present at: {filepath}")

