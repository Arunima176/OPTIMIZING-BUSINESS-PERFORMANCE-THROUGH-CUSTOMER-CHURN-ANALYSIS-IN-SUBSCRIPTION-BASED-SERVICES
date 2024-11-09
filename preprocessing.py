import pandas as pd
import numpy as np
from loading import DataLoader  

class DataPreprocessor:
    def __init__(self, df):
        self.df = df

    def check_info(self):
        print(self.df.info())

    def check_missing_values(self):
        missing_values = self.df.isnull().sum()
        print("Missing values in each column:")
        print(missing_values)

    def convert_total_charges(self):

        try:
            self.df['TotalCharges'] = pd.to_numeric(self.df['TotalCharges'], errors='coerce')
            self.df.loc[self.df['TotalCharges'].isnull(), 'TotalCharges'] = 0
            print("TotalCharges converted and missing values filled.")
        except KeyError:
            print("Error: 'TotalCharges' column not found in the dataframe.")
        except Exception as e:
            print(f"An error occurred while converting 'TotalCharges': {e}")

    def find_duplicates(self):
        duplicate_count = self.df.duplicated().sum()
        print(f"Number of duplicate rows: {duplicate_count}")

    def drop_unwanted_columns(self):

        try:
        
            self.df = self.df.drop(['PhoneService', 'MultipleLines', 'OnlineSecurity', 
                                     'OnlineBackup', 'DeviceProtection', 'TechSupport', 
                                     'StreamingTV', 'StreamingMovies'], axis=1)
            print("Unwanted columns dropped.")
        except KeyError as e:
            print(f"Error: One or more columns to drop were not found: {e}")

    def final_check(self):
        if self.df.isnull().sum().sum() == 0:
            print("No missing values remain in the dataset.")
        else:
            print("There are still missing values in the dataset.")

    def display_shape(self):
        print(f"Dataset shape: {self.df.shape}")


if __name__ == "__main__":

    data_loader = DataLoader(r'C:\Users\aruni\Desktop\customer churn project\Telco-Customer-Churn.csv')  
    df = data_loader.load_data()  

    preprocessor = DataPreprocessor(df)

    preprocessor.check_info()
    preprocessor.check_missing_values()
    preprocessor.convert_total_charges()
    preprocessor.find_duplicates()
    preprocessor.drop_unwanted_columns() 
    preprocessor.display_shape()
    preprocessor.final_check() 




