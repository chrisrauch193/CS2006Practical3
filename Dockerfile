FROM ubuntu:14.04
RUN \
  apt-get update -y && apt-get install -yqq \
  git \
  python \
  python-dev \
  python-pip \
  python-virtualenv && \
  pip install pandas numpy matplotlib matplotlib.pyplot os csv jupyter -yqq \
  git clone https://github.com/chrisrauch193/CS2006Practical3.git -yqq && \

CMD jupyter notebook