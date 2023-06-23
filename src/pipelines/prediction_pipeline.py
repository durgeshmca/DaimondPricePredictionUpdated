import os,sys
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
import pandas as pd
import numpy as np
from src.components.data_transformation import DataTransformationConfig
from src.components.modal_trainer import ModelTrainerConfig

class PredictPipeline:

    def __init__(self):
        pass

    def predict(self,features):
        try:
            #get the file path of preprocessor object and trained model
            preprocessor_config = DataTransformationConfig()
            model_config = ModelTrainerConfig()
            # load preprocessor object and trained model
            preprocessor= load_object(preprocessor_config.preprocessor_obj_file)
            model = load_object(model_config.trained_model_file_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred


        except Exception as e:
            logging.info("Error occured during prediction")
            raise CustomException(e,sys)

class CustomData:

    def __init__(self,
                 carat:float,
                 cut:str,
                 color:str,
                 clarity:str,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float) :
        
        self.carat = carat,
        self.cut = cut,
        self.color = color,
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x =x
        self.y = y
        self.z = z

    def get_data_as_dataframe(self):
        data = {
            'carat':self.carat,
            'cut': self.cut,
            'color': self.color,
            'clarity': self.clarity,
            'depth':self.depth,
            'table':self.table,
            'x': self.x,
            'y': self.y,
            'z': self.z
        }

        df = pd.DataFrame(data)
        return df
                