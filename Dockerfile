FROM ubuntu:14.04

RUN \
  apt-get update -y && apt-get install -yqq \
  git \
  python3 \
  python3-dev \
  python3-pip \
  python-virtualenv && \
  git clone -b docker https://553bd177d76215c8ed19a1c9c7789965394abcb0:x-oauth-basic@github.com/chrisrauch193/CS2006Practical3.git && \
  pip install -r Dependencies/requirements.txt

CMD jupyter notebook