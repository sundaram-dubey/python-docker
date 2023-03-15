FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# uncomment respectiv of which file you need to run
#COPY xmltojson.py .
COPY call-sql-proc.py .

#ENTRYPOINT ["python", "xmltojson.py"]
ENTRYPOINT ["python", "call-sql-proc.py"]

