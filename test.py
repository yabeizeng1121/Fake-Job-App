import joblib

# Load the model
model = joblib.load("model.pkl")

# Test a prediction
print(model.predict(["Sample job description for testing"]))
