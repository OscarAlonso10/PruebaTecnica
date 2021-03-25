FROM python:3.8

COPY requirements.txt .
COPY main.py .
COPY script.py .
COPY start.sh .

RUN pip install -r requirements.txt
