FROM ubuntu:14.04

MAINTAINER Christopher Rauch

RUN apt-get update

RUN apt-get -y install git
RUN git clone https://553bd177d76215c8ed19a1c9c7789965394abcb0:x-oauth-basic@github.com/chrisrauch193/CS2006Practical3.git

RUN apt-get install -y python python-dev python-distribute python-pip python-virtualenv
RUN pip install -r CS2006Practical3/Dependencies/requirements.txt

CMD jupyter notebook