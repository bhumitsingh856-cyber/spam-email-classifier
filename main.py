import sys
import os
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Ensure Python finds clean_text for unpickling
from preprocessing import clean_text
sys.modules['clean_text'] = clean_text

# Load the model
model = joblib.load("./preprocessing/Spam_Model.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailData(BaseModel):
    email: str

from fastapi.responses import FileResponse

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/app")
def serve_ui():
    return FileResponse("index.html")

@app.post("/predict")
def predict(data: EmailData):
    # Pass as a list [data.email]
    print(data)
    prediction = model.predict([data.email])[0]
    return {
        "prediction": int(prediction),
        "is_spam": bool(prediction == 1)
    }
