FROM python:3.9-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
