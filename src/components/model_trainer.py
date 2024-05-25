import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from src.logger.log_setup import logging
from src.exception.exception import CustomException
from src.utils.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        logging.info("Initialized ModelTrainer")

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            logging.info('Data split done')
            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet()
            }

            logging.info('Starting model evaluation')
            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            logging.info(f'Model Report: {model_report}')

            # To get the best model score from the dictionary 
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            logging.info(f'Best Model Found: Model Name: {best_model_name}, R2 Score: {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            logging.info('Model saved successfully')

        except Exception as e:
            logging.error('Exception occurred during Model Training', exc_info=True)
            raise CustomException(e, sys)

