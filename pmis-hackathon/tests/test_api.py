# tests/test_api.py
import requests

def test_predict():
    r = requests.get("http://localhost:8000/predict", timeout=5)
    assert r.status_code == 200
    assert len(r.json()) == 4   # 4 weeks