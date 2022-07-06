FROM python:3.8-slim

WORKDIR /game

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./game

CMD ["python", "./game/main.py"]
