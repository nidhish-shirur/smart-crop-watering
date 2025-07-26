import pandas as pd

# Load the dataset
df = pd.read_csv("dataset.csv")

# Check unique soil types
unique_soil_types = df['soil_type'].unique()
print("Unique Soil Types:")
print(unique_soil_types)
