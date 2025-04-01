import sys
import pandas as pd
import numpy as np
from src.configuration.mongo_db_connection import MongoDBClient
from src.constant import DB_NAME
from typing import Optional

class Proj1Data: 
    """ 
    A class to export MongoDB records as a pandas DataFrame.
    """

    def __init__(self):
        """ 
        Initializes the mongodb Client connection.
        """
        try: 
            self.mongo_client=MongoDBClient(database_name=DB_NAME)
        except Exception as e: 
            raise e
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str]=None)-> pd.DataFrame: 
        """ 
        Exports an entire MongoDB collection as a pandas DataFrame. 
        
        Parameters:
        -----------
        """
        try: 
            if database_name is None: 
                collection=self.mongo_client.database[collection_name]
            else: 
                collection=self.mongo_client[database_name][collection_name]

            # Convert collection data to DataFrame and Process
            print("Fetching data from mongodb")
            df=pd.DataFrame(list(collection.find()))
            print(f"Data fecthed with shape: {df.shape}")

            return df
        except Exception as e: 
            raise e
