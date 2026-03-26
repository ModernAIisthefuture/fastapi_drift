import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv("data/loan.csv")
X = df[["income", "loan_amount", "credit_score"]]
y = df["approved"]

model = RandomForestClassifier()
model.fit(X, y)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)