FROM ubuntu:14.04

RUN \
  apt-get update -y && apt-get install -yqq \
  git \
  python3.6 \
  python3-pip && \
  git clone https://553bd177d76215c8ed19a1c9c7789965394abcb0:x-oauth-basic@github.com/chrisrauch193/CS2006Practical3.git && \
  pip install -r CS2006Practical3/Dependencies/requirements.txt

CMD jupyter notebook