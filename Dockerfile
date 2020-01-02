FROM ubuntu:bionic
##### Do not change the first line #####

COPY ./setup.sh /setup.sh
COPY ./install.sh /install.sh
RUN sh /install.sh && sh /setup.sh
CMD ["/bin/bash"]
