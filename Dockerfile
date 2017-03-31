FROM ubuntu:14.04

MAINTAINER Christopher Rauch

# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

RUN apt-get update

RUN apt-get -y install tar git curl nano wget dialog net-tools build-essential
RUN git clone https://553bd177d76215c8ed19a1c9c7789965394abcb0:x-oauth-basic@github.com/chrisrauch193/CS2006Practical3.git

RUN apt-get install -y python python-dev python-distribute python-pip python-virtualenv
#RUN pip install -r CS2006Practical3/Dependencies/requirements.txt
RUN pip install jupyter

CMD jupyter notebook