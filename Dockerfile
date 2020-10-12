FROM python:3.8-buster

WORKDIR /opt

RUN dnf install python3-pygame

COPY . ./Dino

CMD ["python", "./opt/Dino/main.py"]