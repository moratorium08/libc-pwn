set -eu

dpkg --add-architecture i386
apt-get -y update && apt-get -y upgrade
DEBIAN_FRONTEND="noninteractive" apt-get -y install \
    build-essential \
    python3\
    python3-pip \
    python3-dev \
    git \
    libssl-dev \
    libffi-dev \
    socat \
    procps \
    lib32z1 \
    libc6-dbg \
    libc6-dbg:i386 \
    lib32stdc++6 \
    gdb \
    gdb-multiarch \
    strace \
    ltrace \
    ruby \
    ruby-dev

gem install one_gadget

rm -rf /var/lib/gems/2.*/cache/*
rm -rf /var/lib/apt/list/*

pip3 install --upgrade pwntools
git clone https://github.com/longld/peda.git ~/peda
cd ~/
git clone https://github.com/scwuaptx/Pwngdb.git
cp ~/Pwngdb/.gdbinit ~/
