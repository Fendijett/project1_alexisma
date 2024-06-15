# project1_alexisma

This project analyzes passenger data to provide insights into travel patterns, loyalty membership, and age distributions.

## Features

- Load and clean passenger data
- Calculate average age by travel class
- Plot age distribution, age vs. loyalty, and age distribution by class

## Requirements

- Python 3.x
- pandas
- matplotlib
- seaborn
- plotly

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Fendijett/project1_alexisma.git
    ```

2. Navigate to the project directory:
    ```sh
    cd project1_alexisma
    ```

3. Install the required libraries:
    ```sh
    pip install pandas matplotlib seaborn plotly
    ```

## Usage

1. Ensure your `passengers.csv` file is placed in the project directory.
2. Run the `main_script.py` to generate the plots.

    ```sh
    python main_script.py
    ```

## Script Descriptions

### `passenger_analysis.py`

This script contains the following functions:

- `load_data(file_path)`: Loads the CSV file into a pandas DataFrame.
- `clean_data(df)`: Cleans the data by handling missing values and ensuring appropriate data types.
- `calculate_average_age(df, travel_class)`: Calculates the average age of passengers in a specific travel class and returns a list of loyalty program members.
- `find_loyalty_members(df)`: Returns a list of names of loyalty program members.
- `get_class_statistics(df)`: Returns a dictionary with travel classes as keys and their respective average ages and number of loyalty members as values.
- `plot_age_distribution(df)`: Plots the distribution of ages using a histogram and saves it as `age_distribution.png`.
- `plot_average_age_by_class(df)`: Plots the average age by travel class using a bar chart and saves it as `average_age_by_class.png`.
- `plot_age_vs_loyalty(df)`: Plots a scatter plot of age vs. loyalty membership using Seaborn and saves it as `age_vs_loyalty.png`.
- `plot_age_distribution_by_class(df)`: Plots the distribution of ages for each travel class using a box plot with Plotly and saves it as `age_distribution_by_class.png`.

### `main_script.py`

This script uses the functions from `passenger_analysis.py` to perform the following tasks:

1. Load the passenger data from a CSV file.
2. Clean the data.
3. Calculate average age for a given travel class.
4. Find all loyalty members.
5. Get statistics for all travel classes.
6. Plot age distribution.
7. Plot average age by travel class.
8. Plot age vs. loyalty membership.
9. Plot age distribution by travel class.

## Example Output

After running the `main_script.py`, the following files will be generated in the project directory:

- `age_distribution.png`
- `average_age_by_class.png`
- `age_vs_loyalty.png`
- `age_distribution_by_class.png`
