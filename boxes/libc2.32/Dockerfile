FROM ubuntu:focal
##### Do not change the first line #####

COPY ./setup.sh /setup.sh
COPY ./install.sh /install.sh
COPY ./preinstall.sh /preinstall.sh

ENV DEBIAN_FRONTEND "noninteractive"
RUN sh /preinstall.sh && sh /install.sh && sh /setup.sh
CMD ["/bin/bash"]
