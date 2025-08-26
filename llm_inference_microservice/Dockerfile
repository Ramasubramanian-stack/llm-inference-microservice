# 1. Use official lightweight Python image
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy requirements first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the code
COPY . .

# 6. Command to run API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]