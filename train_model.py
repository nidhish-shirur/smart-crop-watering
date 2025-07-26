import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
df = pd.read_csv("dataset.csv")

# Drop unnecessary columns if any (optional)
# In your case, keeping all except temp and humidity (as per earlier context)
df = df.drop(['temp', 'humidity'], axis=1)

# Encode categorical columns
label_encoders = {}

for column in ['soil_type', 'Seedling Stage', 'crop ID']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Split features and target
X = df[['soil_type', 'Seedling Stage', 'crop ID']]
y = df['result']

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model and encoders
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'encoders.pkl')

print("Model and encoders saved successfully.")
