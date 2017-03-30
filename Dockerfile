FROM ubuntu:14.04
RUN \
  apt-get update -y && apt-get install -yqq \
  git \
  python3 \
  python3-dev \
  python3-pip \
  python-virtualenv && \
  ssh-agent AAAAB3NzaC1yc2EAAAADAQABAAABAQCui5cQHv+mRHff/4M+ji+1kpcpp7G7ftgtODeNJsEWEdLaaboyl8OUXTgJEOyANA18ZeM0CIHpqKkExSOINxhegrIWFJs/r+Pzc8kvZU/It0PEI5J6chFwCcggw7LohM6xIt++DBky/DV8UTYY+fbRGT1MaRc/5FtIMM6YlliX5OBedcGNMPaDlQkYxqWTgwCAW7AC1VDtx8R5ZLF5vRtj+KpxbWY4EEfp4OfpBXEkR0wLK3VyiXN2X9wAsgLByS+jh0XkR+JEeBuRtSr40bcUDpSCuZmun+LpBYZcDWXbs5UciLsH+HtXZKdL2SE8kuZJ1+7VGXPBQvPGhPL9oTwx && \
  git clone https://github.com/chrisrauch193/CS2006Practical3.git && \
  pip install -r Dependencies/requirements.txt

CMD jupyter notebook