from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Create FastAPI instance
app = FastAPI()

# Load HuggingFace model (only once at startup, not every request)
classifier = pipeline("sentiment-analysis")

# Define input format using Pydantic
class TextInput(BaseModel):
    text: str

# Root endpoint (sanity check)
@app.get("/")
def home():
    return {"message": "Welcome to LLM Inference API"}

# Prediction endpoint
@app.post("/predict")
def predict(input: TextInput):
    result = classifier(input.text)[0]   # run model
    return {"label": result["label"], "score": result["score"]}
