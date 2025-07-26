import joblib

encoders = joblib.load("encoders.pkl")
print("Available keys in encoders:", encoders.keys())
