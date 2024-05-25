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
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            data = pd.read_csv(r"""https://raw.githubusercontent.com/nikhilshinde08/End-to-End-Diamond-Prediction/main/Data/train.csv""")
            logging.info("Reading the data frame")
            
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            # Save raw data
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved the raw data in artifact folder")
            
            # Perform train-test split
            train_data, test_data = train_test_split(data, test_size=0.5)
            logging.info("Train-test split completed")
            
            # Save train and test data
            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Saved train and test data in artifact folder")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
