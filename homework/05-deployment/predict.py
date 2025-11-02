import pickle

from fastapi import FastAPI
import uvicorn

from typing import Dict, Any

app = FastAPI(title="Lead conversion")


PIPELINE_PATH = 'pipeline_v1.bin'

with open(PIPELINE_PATH, 'rb') as in_file:
    pipeline = pickle.load(in_file)
    
    
def predict_single(sample):
    score = pipeline.predict_proba(sample)[0, 1]
    return score



@app.post("/predict")
def predict(sample: Dict[str, Any]):
    prob = predict_single(sample)
    return {"convert_probability" : prob}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")