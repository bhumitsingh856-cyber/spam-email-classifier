import sys
import os
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
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


@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/health")
def health():
    return {"status": "ok"}
@app.post("/predict")
def predict(data: EmailData):
    print(data)
    prediction = model.predict([data.email])[0]
    return {
        "prediction": int(prediction),
        "is_spam": bool(prediction == 1)
    }
