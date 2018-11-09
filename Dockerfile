FROM golang:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

ADD . /opt/app

WORKDIR /opt/app

RUN pip3 install -r requirements.txt
RUN make build

ARG vitrine_key
ENV VITRINE_KEY=$vitrine_key

EXPOSE 8000

CMD ["make", "run"]
