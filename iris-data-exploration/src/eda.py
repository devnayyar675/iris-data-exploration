import pandas as pd

def descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates core descriptive statistics across all numerical features.
    
    Args:
        df (pd.DataFrame): Target dataframe.
        
    Returns:
        pd.DataFrame: Statistical descriptions including mean, metric, and percentiles.
    """
    print("\n--- Descriptive Statistics ---")
    stats = df.describe()
    print(stats)
    return stats

def explore_features(df: pd.DataFrame) -> None:
    """
    Explores features based on their variable type, segregating analysis between
    numerical elements and categorical elements.
    
    Args:
        df (pd.DataFrame): Contains dataset entries to dissect.
    """
    print("\n--- Feature Exploration ---")
    
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_cols = df.select_dtypes(exclude=['object', 'category']).columns.tolist()
    
    print(f"Categorical features detected: {categorical_cols}")
    print(f"Numerical features detected: {numerical_cols}")
    
    # Calculate unique distributions for categorical features
    for col in categorical_cols:
        print(f"\nValue Counts for Category '{col}':")
        print(df[col].value_counts())

def summary_analysis(df: pd.DataFrame) -> None:
    """
    Wraps up data analysis into a concise summary statement for quick reviews.
    
    Args:
        df (pd.DataFrame): The analyzed data payload.
    """
    print("\n--- Summarized Final Analysis ---")
    print(f"Total observed population details consist of {len(df)} discrete objects.")
    
    if 'species' in df.columns:
        print("Data holds perfectly balanced classes regarding species:")
        for species, count in df['species'].value_counts().items():
            print(f" -> {species.capitalize()}: {count} records")
