import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models
from dataclasses import dataclass
import sys,os

@dataclass
class ModelTrainerConfig :
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_arr,test_arr):

        try :
            logging.info("Splitting dependent and independent variables from train and test data")
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            models = {
                'LiniearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'ElasticNet':ElasticNet(),
                'DecisionTree':DecisionTreeRegressor(),
                'RandomForest': RandomForestRegressor(),
                'KNearestNeighbour':KNeighborsRegressor()

            }
            model_report:dict = evaluate_models(X_train,y_train,X_test,y_test,models)

            print(f"#############################################\n {model_report} \n##############################\n")
            logging.info(f'Model Report : {model_report}')

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
                ]
            best_model = models[best_model_name]

            print(f"\n Best model found {best_model_name} its R2 score : {best_model_score}\n")
            print("###########################################################################\n")
            logging.info(f"Best model found {best_model_name}, R2 squre score{best_model_score}")

            # save the model object

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

        except Exception as e:
            logging.info('Exception occured in model training stage')
            raise CustomException(e,sys)
