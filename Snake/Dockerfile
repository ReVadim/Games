FROM python:3.8-buster

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./opt/app

CMD ["python", "./opt/app/snakegame.py"]
