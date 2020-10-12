FROM python:3.8-buster

WORKDIR /opt

RUN apt-get install python3-pygame -y

COPY . ./Dino

CMD ["python", "./opt/Dino/main.py"]