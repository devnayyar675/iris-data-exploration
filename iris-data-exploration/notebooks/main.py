import pandas as pd
from src.data_loader import load_data, display_overview, check_missing_values
from src.eda import descriptive_statistics, explore_features, summary_analysis
from src.visualization import generate_scatter_plots, generate_histograms, generate_boxplots

def main():
    print("Starting Iris Data Exploration Project...\n")
    
    # 1. Load Data
    df = load_data('data/iris.csv')
    display_overview(df)
    check_missing_values(df)
    
    # 2. Exploratory Data Analysis
    descriptive_statistics(df)
    explore_features(df)
    summary_analysis(df)
    
    # 3. Data Visualization
    print("\n--- Generating Visualizations ---")
    generate_scatter_plots(df, target_dir="visuals")
    generate_histograms(df, target_dir="visuals")
    generate_boxplots(df, target_dir="visuals")
    print("\nProject executed successfully!")

if __name__ == "__main__":
    main()
