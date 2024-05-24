import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.logger.log_setup import logging
from src.exception.exception import CustomException

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTranformer

from src.utils.utils import save_object

from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataTransformationConfig:
    def __init__(self):

        pass



class DataTransformation:
    def __init__(self):
        pass
    
    def initiate_data_Transformation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
