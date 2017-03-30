FROM ubuntu:14.04
RUN \
  apt-get update -y && \
  apt-get install python python-dev python-pip python-virtualenv -y && \
  apt-get install git && \
  git clone https://github.com/chrisrauch193/CS2006Practical3.git -y && \
  pip install pandas numpy matplotlib matplotlib.pyplot os csv jupyter -y

CMD jupyter notebook -yg
