# 1. Use official Python image
FROM python:3.9-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY app.py .

# 6. Expose Flask port
EXPOSE 5000

# 7. Run the Flask app
CMD ["python", "app.py"]
