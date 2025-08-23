# api/main.py
from pathlib import Path
from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="PMIS-API", version="0.1")

BASE = Path(r"D:\Project-Files\Health-care-hackathon\pmis-hackathon\pmis-hackathon\data\interim")

@app.get("/")
def root():
    return {"message": "PMIS MVP API – Zion Tech Hub Hackathon"}

@app.get("/predict")
def predict():
    df = pd.read_csv(BASE / "burundi_forecast.csv")
    return df.tail(4).to_dict(orient="records")

@app.get("/allocate")
def allocate():
    df = pd.read_csv(BASE / "vax_allocation.csv")
    return df.to_dict(orient="records")