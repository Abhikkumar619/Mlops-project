import os
import sys
import yaml
from src.logger import log
import dill


def read_yaml_file(file_path: str)->dict:
    try:
        with open(file_path,'rb') as yaml_file:
            log.info(f" Yaml file read sucessfully from :{ file_path}") 
            return yaml.safe_load(yaml_file)   
    except Exception as e:
        raise e
    
def save_object(file_path: str, obj:object)->None: 
    try: 
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as filepath:
            dill.dump(obj, filepath)
            log.info(f"Object saved sucessfully at path: {file_path} ")
    except Exception as e: 
        raise e
    
def load_object(file_path:str, obj:object)->object:
    try: 
        with open(file_path,'rb') as filepath: 
            obj=dill.load(filepath)
            log.info(f'object log successfuly from path: {filepath}')
            return obj
    except Exception as e:
        raise e
