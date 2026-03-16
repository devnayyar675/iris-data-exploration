import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads the Iris dataset from a prescribed local path into a Pandas DataFrame.
    
    Args:
        file_path (str): The relative or absolute path to the dataset CSV.
        
    Returns:
        pd.DataFrame: The loaded dataset.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing dataset! Unable to find file at: {file_path}")
    
    print(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    return df

def display_overview(df: pd.DataFrame) -> None:
    """
    Displays a generalized operational overview of the dataset.

    Args:
        df (pd.DataFrame): The target structured matrix.
    """
    print("\n--- Dataset Overview ---")
    print(f"Shape: {df.shape[0]} Rows, {df.shape[1]} Columns")
    print(f"Columns Matrix: {df.columns.tolist()}")
    
    print("\n--- First 5 Rows ---")
    print(df.head())
    
    print("\n--- Dataset Target Info ---")
    df.info()

def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Explores and visualizes the presence of any missing variables throughout the dataset.

    Args:
        df (pd.DataFrame): The data matrix.
        
    Returns:
        pd.Series: Pandas series displaying null counts.
    """
    print("\n--- Missing Value Checking ---")
    missing_data = df.isnull().sum()
    
    if missing_data.sum() == 0:
        print("Success: No missing values found in the dataset.")
    else:
        print(missing_data[missing_data > 0])
        
    return missing_data
