FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY src/ ./src/

EXPOSE 5000

CMD ["python3", "src/app.py"]