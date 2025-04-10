from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run
from typing import Optional
from src.pipeline.training_pipeline import TrainPipeline
from src.constant import APP_HOST, APP_PORT
from src.pipeline.prediction_pipeline import VechicleData, VehicleDataClassifier
import pandas as pd

# Initialize FastAPI application
app=FastAPI()

# Mount the 'static' directory for saving static files like css
app.mount("/static", StaticFiles(directory="static"), name='static')

# Set up jinja2 template engine for rendering HTML templates. 
templates=Jinja2Templates(directory='templates')


# Allow all origins for corss-origin resoucre sharing
origins=['*']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"])

class DataForm: 
    """ 
    DataForm class to handle and process incoming form data. 
    This class define the vechicle related attribites expected from the form. 
    """
    def __init__(self, request: Request): 
        self.request: Request=request
        self.Gender:Optional[int]=None
        self.Age: Optional[int] = None
        self.Driving_License: Optional[int] = None
        self.Region_Code: Optional[float] = None
        self.Previously_Insured: Optional[int] = None
        self.Annual_Premium: Optional[float] = None
        self.Policy_Sales_Channel: Optional[float] = None
        self.Vintage: Optional[int] = None
        self.Vehicle_Age_lt_1_Year: Optional[int] = None
        self.Vehicle_Age_gt_2_Years: Optional[int] = None
        self.Vehicle_Damage_Yes: Optional[int] = None


    async def get_vehicle_data(self): 
        """ 
        Method to retrieve and assign from data to class atribites. 
        This method is asunchronous to handle from data feteching eithout blocking. 
        """
        form=await self.request.form()
        self.Gender= form.get('Gender')
        self.Age=form.get('Age')
        self.Driving_License=form.get('Driving_License')
        self.Region_Code = form.get("Region_Code")
        self.Previously_Insured = form.get("Previously_Insured")
        self.Annual_Premium = form.get("Annual_Premium")
        self.Policy_Sales_Channel = form.get("Policy_Sales_Channel")
        self.Vintage = form.get("Vintage")
        self.Vehicle_Age_lt_1_Year = form.get("Vehicle_Age_lt_1_Year")
        self.Vehicle_Age_gt_2_Years = form.get("Vehicle_Age_gt_2_Years")
        self.Vehicle_Damage_Yes = form.get("Vehicle_Damage_Yes")


    
@app.get("/", tags=['authentication'])
async def index(request: Request): 
    """ 
    Renders the main HTML form page for vechicle data input.
    """
    return templates.TemplateResponse(
        "vehicledata.html",{"request": request, "context": "Rendering"})

@app.post("/")
async def predictRoutclient(request: Request): 
    """ 
    Endpoint to receive form data, processit, and make prediction,. 
    """
    try: 
        form=DataForm(request)
        await form.get_vehicle_data()

        vehicle_data= VechicleData(
            Gender=form.Gender, 
            Age = form.Age,
            Driving_License = form.Driving_License,
            Region_Code = form.Region_Code,
            Previously_Insured = form.Previously_Insured,
            Annual_Premium = form.Annual_Premium,
            Policy_Sales_Channel = form.Policy_Sales_Channel,
            Vintage = form.Vintage,
            Vehicle_Age_lt_1_Year = form.Vehicle_Age_lt_1_Year,
            Vehicle_Age_gt_2_Years = form.Vehicle_Age_gt_2_Years,
            Vehicle_Damage_Yes = form.Vehicle_Damage_Yes
            )
        # Convet form data into a DataFrmae for the model
        vechicle_df=vehicle_data.get_vehicle_data_as_dict()
        vechicle_df['id']=1
        vechicle_df=pd.DataFrame.from_dict(vechicle_df)

      
        # Initialize the prediction pipeline. 
        model_predictor= VehicleDataClassifier()

        value= model_predictor.predict(dataframe=vechicle_df)[0]
        # Interpret the prediction result as 'Response-Yes' or 'Response-No'
        status = "Response-Yes" if value == 1 else "Response-No"

            # Render the same HTML page with the prediction result
        return templates.TemplateResponse(
                "vehicledata.html",
                {"request": request, "context": status})
    except Exception as e: 
        raise e
    
    

# Main entry point to start the FastAPI server
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)