import sqlite3
from datetime import datetime

DB_PATH = "db/loan_app.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Predictions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        income REAL,
        loan_amount REAL,
        credit_score REAL,
        loan_approved INTEGER,
        timestamp TEXT
    )
    """)

    # Drift metrics table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS drift_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        feature TEXT,
        statistic REAL,
        p_value REAL,
        drift_detected INTEGER,
        timestamp TEXT
    )
    """)
    conn.commit()
    conn.close()

def log_prediction(income, loan_amount, credit_score, loan_approved):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO predictions (income, loan_amount, credit_score, loan_approved, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (income, loan_amount, credit_score, loan_approved, datetime.now()))
    conn.commit()
    conn.close()

def log_drift(drift_report):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for feature, values in drift_report.items():
        cursor.execute("""
            INSERT INTO drift_metrics (feature, statistic, p_value, drift_detected, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (feature, values["statistic"], values["p_value"], int(values["drift_detected"]), datetime.now()))
    conn.commit()
    conn.close()