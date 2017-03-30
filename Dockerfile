FROM ubuntu:14.04
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  apt-get install git && \
  git clone https://github.com/chrisrauch193/CS2006Practical3.git && \
  pip install pandas numpy matplotlib matplotlib.pyplot os csv jupyter

CMD jupyter notebook && \
    Y
