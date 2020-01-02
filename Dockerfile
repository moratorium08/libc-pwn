FROM ubuntu:bionic
##### Do not change the first line #####

COPY ./setup.sh /setup.sh

RUN apt-get update && apt-get upgrade &&\
    apt-get -y install \
        python2.7 \
        python-pip \
        python-dev \
        git \
        libssl-dev \
        libffi-dev \
        socat \
        procps && \
    pip install --upgrade pwntools &&\
    git clone https://github.com/longld/peda.git ~/peda &&\
    cd ~/ &&\
    git clone https://github.com/scwuaptx/Pwngdb.git &&\
    cp ~/Pwngdb/.gdbinit ~/ &&\
    sh /setup.sh

CMD ["/bin/bash"]
