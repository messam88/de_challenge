FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY load-csv.py ./

ENTRYPOINT [ "python", "load-csv.py" ]