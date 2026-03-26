import pandas as pd
from scipy.stats import ks_2samp

# Reference data
ref_df = pd.read_csv("data/loan.csv")

def check_drift(new_data):
    drift_report = {}
    for col in ["income", "loan_amount", "credit_score"]:
        stat, p_value = ks_2samp(ref_df[col], new_data[col])
        drift_report[col] = {
            "statistic": float(stat),           # convert numpy.float64 → float
            "p_value": float(p_value),          # convert numpy.float64 → float
            "drift_detected": bool(p_value < 0.05)  # convert numpy.bool_ → bool
        }
    return drift_report
