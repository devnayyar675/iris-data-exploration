# Exploring and Visualizing the Iris Dataset

## Project Overview
This repository contains a complete Exploratory Data Analysis (EDA) of the classic Iris dataset. The project demonstrates a structured approach to analyzing datasets, from data ingestion and cleaning to statistical summarization and visualization, following real-world data science repository standards.

## Task Objective
The primary objective of this project is to learn how to properly load, inspect, and visualize a dataset. This includes uncovering trends, understanding data distributions, and evaluating correlations and relationships between different features.

## Dataset Description
The **Iris Dataset** is a classic machine learning dataset that includes 150 instances of Iris flowers from three different species: *Setosa*, *Versicolor*, and *Virginica*. 
Each instance contains 4 features:
* `sepal_length`: Length of the sepal (in cm)
* `sepal_width`: Width of the sepal (in cm)
* `petal_length`: Length of the petal (in cm)
* `petal_width`: Width of the petal (in cm)

## Technologies Used
- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and loading
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebook**: Interactive data exploration environments

## Repository Structure
```text
iris-data-exploration/
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files for git tracking
├── data/                  # Contains the raw CSV datasets
├── notebooks/             # Iterative Jupyter Python notebooks
├── src/                   # Source code modules (data loading, EDA, plots)
├── visuals/               # Location for saving generated image visualisations
└── reports/               # Markdown reports and generated insights
```

## Data Analysis Workflow
1. **Data Loading:** Read `iris.csv` gracefully using pandas.
2. **Data Inspection:** Inspect columns, data types, dataset shape, and verify null counts.
3. **Exploratory Data Analysis (EDA):** Perform descriptive statistical analysis across categorical and numerical features.
4. **Visualisation:** Create graphical components to interpret numeric relationships.

## Visualizations Created
* **Scatter Plots**: Compare `sepal_length` vs `sepal_width`, and `petal_length` vs `petal_width` colored by species.
* **Histograms**: Determine distribution contours of individual numeric features.
* **Box Plots**: Highlight central tendencies and visual outlier detection.

## Key Insights
* The *Setosa* species is highly separable from the others relying purely on its petal dimensions.
* There is a strong linear correlation between petal length and petal width.
* Some outliers exist in *Setosa*'s sepal widths, which require careful handling in modeling pipelines.

## Installation Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/iris-data-exploration.git
   cd iris-data-exploration
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Project
* **Jupyter Notebook:** To browse the interactive data report, launch:
  ```bash
  jupyter notebook notebooks/iris_data_exploration.ipynb
  ```
* **Python Scripts:** The modular source code lets you test pipelines programmatically. You can load and visualize the data dynamically using functions inside the `/src` package.
