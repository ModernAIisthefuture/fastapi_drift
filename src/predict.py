import pickle
import numpy as np

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_loan(data):
    features = np.array([[data.income, data.loan_amount, data.credit_score]])
    prediction = model.predict(features)[0]
    return int(prediction)