import pandas as pd

def load_data(file_path):

    #Load the CSV file into a pandas DataFrame.
    
    # Loading the CSV file, skipping the first row because of no titles for each column
    df = pd.read_csv(file_path, skiprows=1, header=None)
    
    # Defining the correct column titles
    df.columns = ['PassengerID', 'Name', 'Birthdate', 'TravelClass', 'LoyaltyMember', 'FlightNumber']
    
    return df

def clean_data(df):
    
    #Clean the data by checking for and handling missing values and ensuring appropriate data types.
    

    print("Columns in DataFrame:", df.columns)
    
    
    df.dropna(inplace=True)
    
    df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')
    df['LoyaltyMember'] = df['LoyaltyMember'].astype(bool)
    
    # Dropped rows where 'Birthdate' couldn't be converted
    df = df[df['Birthdate'].notna()]
    
    return df

file_path = 'C:/Users/milks/Desktop/project_alexisma/passengers.csv'
df = load_data(file_path)

print("First few rows of the DataFrame:\n", df.head())

cleaned_df = clean_data(df)
print(cleaned_df.head())

print("         ")
print("         ")
print("         ")
print("         ")
########################################################################
import pandas as pd
from datetime import datetime

def calculate_average_age(df, travel_class):
    
    # passengers based on travel class
    class_passengers = df[df['TravelClass'] == travel_class]
    
    # age
    current_year = datetime.now().year
    class_passengers['Age'] = current_year - class_passengers['Birthdate'].dt.year
    
    # average age
    average_age = class_passengers['Age'].mean()
    
    # names of loyalty program members
    loyalty_members = class_passengers[class_passengers['LoyaltyMember'] == True]['Name'].tolist()
    
    return average_age, loyalty_members

def find_loyalty_members(df):

    # Filter passengers who are loyalty program members
    loyalty_members = df[df['LoyaltyMember'] == True]['Name'].tolist()
    
    return loyalty_members

file_path = 'C:/Users/milks/Desktop/project_alexisma/passengers.csv'  # Update with your file path
df = load_data(file_path)

df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')

cleaned_df = clean_data(df)

# average age for a given travel class
average_age, loyalty_members_in_class = calculate_average_age(cleaned_df, 'Economy')
print(f"Average age in Economy class: {average_age}")
print("Loyalty members in Economy class:", loyalty_members_in_class)

# Find all loyalty members
all_loyalty_members = find_loyalty_members(cleaned_df)
print("All loyalty members:", all_loyalty_members)
print("         ")
print("         ")
print("         ")
print("         ")
########################################################################
import pandas as pd
from datetime import datetime

def get_class_statistics(df):
    
    class_stats = {}
    travel_classes = df['TravelClass'].unique()
    
    current_year = datetime.now().year
    
    for travel_class in travel_classes:
        class_passengers = df[df['TravelClass'] == travel_class]
        class_passengers['Age'] = current_year - class_passengers['Birthdate'].dt.year
        average_age = class_passengers['Age'].mean()
        loyalty_members_count = class_passengers[class_passengers['LoyaltyMember'] == True].shape[0]
        
        class_stats[travel_class] = {
            'Average Age': average_age,
            'Loyalty Members': loyalty_members_count
        }
    
    return class_stats
