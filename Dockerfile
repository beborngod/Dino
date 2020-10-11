FROM python:3.8-buster

WORKDIR /opt

RUN pip install pygame

COPY ../Dino

CMD ["python", "./main.py"]