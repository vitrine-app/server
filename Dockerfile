FROM golang:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev python3-mysqldb build-essential

ARG vitrine_key
ENV VITRINE_KEY=$vitrine_key

ADD . /opt/app

WORKDIR /opt/app

RUN pip3 install -r requirements.txt
RUN make build

EXPOSE 8000

CMD ["make", "run"]
