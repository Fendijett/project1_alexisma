import os
import passenger_analysis as pa
import pandas as pd

print(os.listdir('.'))

print("Available functions in passenger_analysis:", dir(pa))

file_path = 'C:/Users/milks/Desktop/project_alexisma/passengers.csv'

df = pa.load_data(file_path)

df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')

cleaned_df = pa.clean_data(df)

average_age, loyalty_members_in_class = pa.calculate_average_age(cleaned_df, 'Economy')
print(f"Average age in Economy class: {average_age}")
print("Loyalty members in Economy class:", loyalty_members_in_class)

all_loyalty_members = pa.find_loyalty_members(cleaned_df)
print("All loyalty members:", all_loyalty_members)

class_statistics = pa.get_class_statistics(cleaned_df)
print("Class statistics:", class_statistics)

print("Calling plot_age_distribution function...")
pa.plot_age_distribution(cleaned_df)

print("Calling plot_average_age_by_class function...")
pa.plot_average_age_by_class(cleaned_df)
###
print("Calling plot_age_vs_loyalty function...")
pa.plot_age_vs_loyalty(cleaned_df)


print("Calling plot_age_distribution_by_class function...")
pa.plot_age_distribution_by_class(cleaned_df)