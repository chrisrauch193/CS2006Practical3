FROM ubuntu:14.04
RUN \
  apt-get update -y && apt-get install -yqq \
  git \
  python \
  python-dev \
  python-pip \
  python-virtualenv
