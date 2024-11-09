import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        """Initialize the DataLoader with the file path."""
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load the dataset from the specified file path."""
        try:
            self.data = pd.read_csv(self.file_path)
            return self.data
        except FileNotFoundError:
            raise FileNotFoundError(f"File at path {self.file_path} was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {str(e)}")

    def display_head(self, num_rows=5):
        """Display the first few rows of the dataset."""
        if self.data is not None:
            return self.data.head(num_rows)
        else:
            raise ValueError("Data not loaded. Please call load_data() first.")

    def display_shape(self):
        """Display the shape of the dataset."""
        if self.data is not None:
            return self.data.shape
        else:
            raise ValueError("Data not loaded. Please call load_data() first.")

    def display_summary(self):
        """Display summary statistics of the dataset."""
        if self.data is not None:
            return self.data.describe(include='all')
        else:
            raise ValueError("Data not loaded. Please call load_data() first.")

 

# Usage
if __name__ == "__main__":
    try:
        # Create an instance of DataLoader with the dataset path
        loader = DataLoader(r'C:\Users\aruni\Desktop\customer churn project\Telco-Customer-Churn.csv')
        
        # Load the dataset
        data = loader.load_data()
        
        # Display the first few rows of the dataset
        print("First few rows of the dataset:")
        print(loader.display_head())
        
        # Display the shape of the dataset
        print("Dataset shape:", loader.display_shape())
        
        # Display summary statistics
        print("Summary statistics:")
        print(loader.display_summary())
 

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except FileNotFoundError as fnf_error:
        print(f"FileNotFoundError: {fnf_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")






