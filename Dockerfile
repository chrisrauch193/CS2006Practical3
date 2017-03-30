FROM ubuntu:14.04
RUN \
  apt-get update -y && apt-get install -yqq \
  git \
  python3 \
  python3-dev \
  python3-pip \
  python3-virtualenv && \
  pip install -r requirements

CMD jupyter notebook