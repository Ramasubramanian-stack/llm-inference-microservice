# LLM Inference Microservice 🚀

A FastAPI-based microservice that serves a HuggingFace sentiment analysis model, containerized with Docker.

## Features
- REST API built with FastAPI
- Sentiment Analysis using HuggingFace Transformers (DistilBERT)
- Dockerized for portability
- Swagger UI auto-generated (`/docs`)

## Endpoints
- `GET /` → Health check
- `POST /predict` → Run sentiment analysis

### Example Request
```json
POST /predict
{
  "text": "I love learning with FastAPI!"
}
