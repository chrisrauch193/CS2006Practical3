FROM ubuntu:14.04
RUN \
  apt-get update -y && apt-get install -yqq \
  git \
  python3 \
  python3-dev \
  python3-pip \
  python-virtualenv && \
  git clone https://github.com/chrisrauch193/CS2006Practical3.git -yqq && \
  pip install -r Dependencies/requirements.txt

CMD jupyter notebook