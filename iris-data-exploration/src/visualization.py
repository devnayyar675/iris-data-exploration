import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def ensure_save_directory(directory: str) -> None:
    """Ensures that the directory to save visuals exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_scatter_plots(df: pd.DataFrame, target_dir: str = "visuals") -> None:
    """
    Generates and saves feature relationship scatter plots.
    
    Args:
        df (pd.DataFrame): The loaded dataset.
        target_dir (str): Relative directory mapping to save PNG assets.
    """
    ensure_save_directory(target_dir)
    sns.set_theme(style="whitegrid")

    # 1. Sepal Dimension Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", s=80)
    plt.title("Relationship Map: Sepal Length vs Sepal Width")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Sepal Width (cm)")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.savefig(os.path.join(target_dir, "scatter_sepal_dimensions.png"))
    plt.close()

    # 2. Petal Dimension Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species", s=80)
    plt.title("Relationship Map: Petal Length vs Petal Width")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.savefig(os.path.join(target_dir, "scatter_petal_dimensions.png"))
    plt.close()
    
    print(f"[Done] Saved Scatter plots to '{target_dir}/'")

def generate_histograms(df: pd.DataFrame, target_dir: str = "visuals") -> None:
    """
    Plots analytical distribution histograms for numeric metrics.
    """
    ensure_save_directory(target_dir)
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True, bins=20, color="royalblue")
        plt.title(f"Data Distribution analysis: {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.tight_layout()
        
        # Format filename reliably
        safe_col_name = col.replace('.', '_')
        plt.savefig(os.path.join(target_dir, f"histogram_distribution_{safe_col_name}.png"))
        plt.close()
        
    print(f"[Done] Saved Feature Histograms to '{target_dir}/'")

def generate_boxplots(df: pd.DataFrame, target_dir: str = "visuals") -> None:
    """
    Prepares standard box and whisker plots useful for visual outlier detection.
    """
    ensure_save_directory(target_dir)
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x="species", y=col, data=df, palette="husl")
        plt.title(f"Box Plot Mapping Outliers: {col} broken down by Species")
        plt.tight_layout()
        
        safe_col_name = col.replace('.', '_')
        plt.savefig(os.path.join(target_dir, f"boxplot_variance_{safe_col_name}.png"))
        plt.close()
        
    print(f"[Done] Saved Box Plots to '{target_dir}/'")
