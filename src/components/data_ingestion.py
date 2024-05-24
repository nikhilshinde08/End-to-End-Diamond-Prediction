import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.logger.log_setup import logging
from src.exception.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    def __init__(self):
        pass




class DataIngestion:
    def __init__(self):
        pass
    
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
