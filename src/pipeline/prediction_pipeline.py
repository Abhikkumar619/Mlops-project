import sys
from src.entity.config_entity import VehiclePredictorConfig
from src.entity.s3_estimator import Proj1Estimator
from src.logger import log
from pandas import DataFrame

class VechicleData: 
    def __init__(self, 
                 Gender, 
                 Age, 
                 Driving_License,
                Region_Code,
                Previously_Insured,
                Annual_Premium,
                Policy_Sales_Channel,
                Vintage,
                Vehicle_Age_lt_1_Year,
                Vehicle_Age_gt_2_Years,
                Vehicle_Damage_Yes):
        """ 
        Vehicles Data constructor
        Input: all features of the trained model for predication.
    
        """
        try: 
            self.Gender=Gender
            self.Gender = Gender
            self.Age = Age
            self.Driving_License = Driving_License
            self.Region_Code = Region_Code
            self.Previously_Insured = Previously_Insured
            self.Annual_Premium = Annual_Premium
            self.Policy_Sales_Channel = Policy_Sales_Channel
            self.Vintage = Vintage
            self.Vehicle_Age_lt_1_Year = Vehicle_Age_lt_1_Year
            self.Vehicle_Age_gt_2_Years = Vehicle_Age_gt_2_Years
            self.Vehicle_Damage_Yes = Vehicle_Damage_Yes


        except Exception as e: 
            raise e
        
    def get_vechicle_input_data_frame(self)->DataFrame: 
        """ 
        This function returns a dataframe from DataForm.
        """
        try: 
            vechicle_input_data=self.get_vechicle_input_data_frame()
            return DataFrame(vechicle_input_data)
        except Exception as e: 
            raise e
        
    def get_vehicle_data_as_dict(self): 
        """ 
        This function returns a dictionary from vechicledaa class input
        """
        try: 
            input_data={
                "Gender":[self.Gender], 
                "Age": [self.Age],
                "Age": [self.Age],
                "Driving_License": [self.Driving_License],
                "Region_Code": [self.Region_Code],
                "Previously_Insured": [self.Previously_Insured],
                "Annual_Premium": [self.Annual_Premium],
                "Policy_Sales_Channel": [self.Policy_Sales_Channel],
                "Vintage": [self.Vintage],
                "Vehicle_Age_lt_1_Year": [self.Vehicle_Age_lt_1_Year],
                "Vehicle_Age_gt_2_Years": [self.Vehicle_Age_gt_2_Years],
                "Vehicle_Damage_Yes": [self.Vehicle_Damage_Yes]}
            
            log.info(f"Created vehicle data dict")
            log.info(f"Exited get vehicle data as dict method as VechicleData class")
            return input_data
        
        except Exception as e: 
            raise e
class VehicleDataClassifier: 
    def __init__(self, prediction_pipeline_config:VehiclePredictorConfig=VehiclePredictorConfig())->None:
        """ 
        :para prediction_pipeline_config: Configuration for prediction the value.
        """
        try: 
            self.prediction_pipeline_config=prediction_pipeline_config
        except Exception as e: 
            raise e
        

    def predict(self, dataframe)->str: 
        """ 
        This is the method of VechicleDataClassifier
        returns: Prediction in string format. 
        """

        try: 
            log.info(f"Entered predict method of VehicleDataClassifier")
            model= Proj1Estimator(bucket_name=self.prediction_pipeline_config.model_bucket_name, 
                                  model_path=self.prediction_pipeline_config.model_file_path)
            result=model.predict(dataframe)
            return result
        except Exception as e: 
            raise e