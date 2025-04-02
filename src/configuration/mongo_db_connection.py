import os
import sys
import pymongo
from constant import *
from logger import log
from pymongo.mongo_client import MongoClient
import pandas as pd
import certifi
from dotenv import load_dotenv
load_dotenv()

# Load the certificate authority file to avoid timeout errors when connecting to MongoDB
ca = certifi.where()

class MongoDBClient: 
    """
    MongoDBClient is responsiable for establishing a connection to the mongoDB database.

    Attributes:
    ------------
    client: MongoClient
        A shared mongoclient for the class. 

    database: Database
        The specific database instance that MongoDBClient connects to. 

    Methods: 
    ---------
    __init__(database_name: str)-> None
        Initializes the mongodb connection using the given database name.
    """

    client=None

    def __init__(self, database_name=DB_NAME)->None:
        """ 
        Initializes a connection to the mongodb database. if not existing connection is found, it establishes a new one.
        
        parameters: 
        -----------
        database_name: str, optional
            name of the monodb database to. Default is set by DATABASE_NAME constant. 

        Raises: 
        -------
        If there is an issue connecting to mongogb or if the environment variable for the mongodb url is not set. 
    
        """
        try: 
            if MongoDBClient.client is None: 
                    mongo_uri=os.getenv('MONGO_URL')
                    if mongo_uri is None:
                        raise Exception("Environement variable is not set")
                    
            MongoDBClient.client=MongoClient(mongo_uri)
            log.info("Connecting to mongodbdata_Base")
            log.info(f"Client Information: {MongoDBClient.client}")

            # Now connecting to the specific database and collection
            self.client=MongoDBClient.client
            self.database=self.client[database_name]

            log.info("Mongodb connecting sucessfully.")
        except Exception as e: 
            raise e