from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from src.predict import predict_loan
from src.drift import check_drift

app = FastAPI(title="Loan API with Data Drift Detection")

class LoanRequest(BaseModel):
    income: float
    loan_amount: float
    credit_score: float

@app.get("/")
def home():
    return {"message": "Loan API Running 🚀"}

@app.post("/predict")
def predict(request: LoanRequest):
    result = predict_loan(request)
    return {"loan_approved": result}

@app.post("/drift")
def drift(data: list[LoanRequest]):
    new_df = pd.DataFrame([d.dict() for d in data])
    drift_report = check_drift(new_df)
    return drift_report
