#!/bin/bash
set -e

echo "Install Python >>>>>>>>>>>>>>"
sudo apt-get install -y python3.8 python3.8-dev python3.8-venv python3-pip      #Install Python3

# install docker 
echo "Install Docker >>>>>>>>>>>>>>"
sudo snap install docker            #Install Docker
sudo snap connect docker:home       #Docker Home


echo "Install PIP3 >>>>>>>>>>>>>>"
sudo pip3 install --upgrade virtualenv          #Install PIP

# get parent dir
home="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/../ && pwd )/HR_Management"


# installs project dependencies
# delete Python virtual environment and recreate it
rm -rf $home/env
# Do something under GNU/Linux platform
virtualenv --python=python3.8 $home/env
echo "export PYTHONPATH='$home'" >> $home/env/bin/activate
# enter the venv and install dependencies
source $home/env/bin/activate


pip install -r $home/requirements.txt

# down docker compose and up it again
echo "RUN Docker >>>>>>>>>>>>>>"
sudo docker-compose  -f docker-compose.yml up -d db admin


