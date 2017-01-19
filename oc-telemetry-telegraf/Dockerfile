FROM golang:1.6.2-wheezy

RUN mkdir /go/src/github.com
RUN mkdir /go/src/github.com/influxdata
WORKDIR /go/src/github.com/influxdata

RUN go get -u -v google.golang.org/grpc

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install envtpl

ENV DATE 20170118

RUN git clone https://github.com/ajhai/telegraf.git

WORKDIR /go/src/github.com/influxdata/telegraf

RUN make

CMD /go/bin/telegraf -debug
