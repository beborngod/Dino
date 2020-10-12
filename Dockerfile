FROM python:3.8-buster

WORKDIR /opt

RUN apt-get update

RUN apt-get install python3-pygame -y

RUN apt-get autoremove

COPY . ./Dino

CMD ["python", "main.py"]