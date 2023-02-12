FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY load-schema.py ./
COPY schema.sql ./

ENTRYPOINT [ "python", "load-schema.py" ]
