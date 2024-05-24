import pandas as pd
import numpy as np
import sys
import os
from sklearn.metrics import mean_absolute_error,median_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import pickle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.logger.log_setup import logging
from src.exception.exception import CustomException
from src.utils.utils import save_object
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ModelEvaluationConfig:
        pass 
   



class ModelEvaluation:
    def __init__(self):
        pass
    
    def initiate_data_Evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
