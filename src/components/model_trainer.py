import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.logger.log_setup import logging
from src.exception.exception import CustomException
from src.utils.utils import save_object,evaluate_model
from dataclasses import dataclass
from pathlib import Path

from sklearn.linear_model import LinearRegression,Ridge,Lasso



@dataclass
class ModelTrainerConfig:
    pass



class ModelTrainer:
    def __init__(self):
        pass


    def initiate_model_training(self):
    
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
