# ! /bin/bash

apt-get -y update
apt-get install -y git python python-pip
git clone https://github.com/dlux/algorithms.git
chwon -r ubuntu:ubuntu algorithms
pushd algorithms
pip install -e ./
