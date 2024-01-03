FROM ubuntu:latest

WORKDIR /$(pwd)


ADD . /$(pwd)


RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install pip
RUN pip install flask
RUN pip install requests


EXPOSE 9945

CMD ["python3","app.py"]
