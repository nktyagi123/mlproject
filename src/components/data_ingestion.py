import os
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()

    def iniate_data_ingestion(self):
        logging.info("Entered into the Data Ingestion Method and Component...")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as Dataframe..")

            os.makedirs(os.path.dirname(self.ingestionconfig.train_data_path),exist_ok=True)
            df.to_csv(self.ingestionconfig.raw_data_path, index=False, header=True)

            logging.info("Train Test split started..")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestionconfig.train_data_path,index=False, header = True)
            test_set.to_csv(self.ingestionconfig.test_data_path,index=False, header = True)

            logging.info("Ingestion of the data is Completed..")

            return(
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path
            )
    
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = DataIngestion()
    obj.iniate_data_ingestion()
            