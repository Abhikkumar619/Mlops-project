import boto3
from src.configuration.aws_connection import S3Client
from mypy_boto3_s3.service_resource import Bucket



class SimpleStorageService: 
    """ 
    A class for interacting with aws s3 storage, proving methods for file management, 
    data uploads, and data retrival in s3 buckets. 
    """

    def __init__(self):
        """ 
        Initializes the SimpleStorageService instance with s3 resource and client
        from the s3client class. 
        """
        s3_client=S3Client()
        self.s3_resource=s3_client.s3_resource
        self.s3_client=s3_client.s3_client


    
    
    def get_bucket(self, bucket_name: str)->Bucket:
        """
        Retrivers the s3 bucket based on the provided bucket name.

        Args: 
            bucket_name (str) : The name of the s3 bucket. 
        
        Returns: 
            Bucket: S3 bucket object 

        """
        pass


    