import os
import sys
import yaml
from src.logger import log
import dill
import numpy as np


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
    
def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise e
