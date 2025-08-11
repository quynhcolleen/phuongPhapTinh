
FROM python:3.12 AS development

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./main.py"] 
