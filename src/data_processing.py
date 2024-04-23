import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException

from sklearn.model import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_path: str = os.path.join('data', 'train.csv')
    test_path: str = os.path.join('data', 'test.csv')
    raw_path: str = os.path.join('data', 'raw.csv')

class DataIngestion:
    def __init__(self) -> None:
        self.config = DataIngestionConfig()

    def read_data(self, path: str) -> pd.DataFrame:
        logging.info(f"Reading data from {path}")
        try:
            return pd.read_csv(path)
        except Exception as e:
            logging.error(f"Error reading data from {path}")
            raise CustomException(f"Error reading data from {path}")

    def train_test_split(self, data: pd.DataFrame) -> pd.DataFrame:
        logging.info("Splitting data into train and test")
        try:
            train, test = train_test_split(data, test_size=0.2, random_state=42)
            train.to_csv(self.config.train_path, index=False)
            test.to_csv(self.config.test_path, index=False)

            return train, test
        except Exception as e:
            logging.error("Error splitting data into train and test")
            raise CustomException("Error splitting data into train and test")

if __name__ == "__main__":
    data_ingestion = DataIngestion()
    raw_data = data_ingestion.read_data(data_ingestion.config.raw_path)
    train_data, test_data = data_ingestion.train_test_split(raw_data)
    logging.info("Data ingestion completed successfully")
