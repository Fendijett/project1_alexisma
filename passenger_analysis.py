import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    df = pd.read_csv(file_path, skiprows=1, header=None, on_bad_lines='skip')
    df.columns = ['PassengerID', 'Name', 'Birthdate', 'TravelClass', 'LoyaltyMember', 'FlightNumber']
    return df

def clean_data(df):
    df.dropna(inplace=True)
    df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')
    df['LoyaltyMember'] = df['LoyaltyMember'].astype(bool)
    df = df[df['Birthdate'].notna()]
    return df

def calculate_average_age(df, travel_class):
    class_passengers = df[df['TravelClass'] == travel_class].copy()
    current_year = datetime.now().year
    class_passengers.loc[:, 'Age'] = current_year - class_passengers['Birthdate'].dt.year
    average_age = class_passengers['Age'].mean()
    loyalty_members = class_passengers[class_passengers['LoyaltyMember'] == True]['Name'].tolist()
    return average_age, loyalty_members

def find_loyalty_members(df):
    loyalty_members = df[df['LoyaltyMember'] == True]['Name'].tolist()
    return loyalty_members

def get_class_statistics(df):
    class_stats = {}
    travel_classes = df['TravelClass'].unique()
    current_year = datetime.now().year
    
    for travel_class in travel_classes:
        class_passengers = df[df['TravelClass'] == travel_class].copy()
        class_passengers.loc[:, 'Age'] = current_year - class_passengers['Birthdate'].dt.year
        average_age = class_passengers['Age'].mean()
        loyalty_members_count = class_passengers[class_passengers['LoyaltyMember'] == True].shape[0]
        class_stats[travel_class] = {
            'Average Age': average_age,
            'Loyalty Members': loyalty_members_count
        }
    
    print("Class statistics:", class_stats)  # Debugging
    return class_stats

def plot_age_distribution(df):
    current_year = datetime.now().year
    df.loc[:, 'Age'] = current_year - df['Birthdate'].dt.year
    plt.figure(figsize=(10, 6))
    plt.hist(df['Age'], bins=20, edgecolor='black')
    plt.title('Age Distribution of Passengers')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig('age_distribution.png')
    plt.close()

def plot_average_age_by_class(df):
    class_stats = get_class_statistics(df)
    if class_stats is None:
        print("Class statistics is None")  # Debugging
    else:
        print("Class statistics:", class_stats)  # Debugging
    classes = list(class_stats.keys())
    average_ages = [class_stats[cls]['Average Age'] for cls in classes]
    plt.figure(figsize=(10, 6))
    plt.bar(classes, average_ages, color=['blue', 'green', 'red'])
    plt.title('Average Age by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Average Age')
    plt.savefig('average_age_by_class.png')
    plt.close()
######
def plot_age_vs_loyalty(df):
    """
    Plot a scatter plot of age vs. loyalty membership using Seaborn and save it as age_vs_loyalty.png.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing passenger data
    """
    current_year = datetime.now().year
    df.loc[:, 'Age'] = current_year - df['Birthdate'].dt.year
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Age', y='LoyaltyMember', hue='LoyaltyMember')
    plt.title('Age vs. Loyalty Membership')
    plt.xlabel('Age')
    plt.ylabel('Loyalty Membership')
    plt.savefig('age_vs_loyalty.png')
    plt.close()

def plot_age_distribution_by_class(df):
    """
    Plot the distribution of ages for each travel class using a box plot with Plotly and save it as age_distribution_by_class.png.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing passenger data
    """
    current_year = datetime.now().year
    df.loc[:, 'Age'] = current_year - df['Birthdate'].dt.year
    fig = px.box(df, x='TravelClass', y='Age', points="all")
    fig.update_layout(title='Age Distribution by Travel Class', xaxis_title='Travel Class', yaxis_title='Age')
    fig.write_image('age_distribution_by_class.png')
