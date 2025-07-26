import pandas as pd

# Load the dataset
df = pd.read_csv('dataset.csv')  # Adjust path if needed

# Check the column names
print("Available columns:", df.columns)

# Print unique values in the 'Seedling Stage' column
if 'Seedling Stage' in df.columns:
    print("\nUnique seedling stages:")
    print(df['Seedling Stage'].unique())
else:
    print("\nColumn 'Seedling Stage' not found in dataset.")
