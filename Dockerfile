FROM python:buster

WORKDIR /app

# Get required files
COPY ./main.py .
COPY ./requirements.txt .

# Install deps
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
