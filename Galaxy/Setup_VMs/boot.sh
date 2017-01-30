#!/usr/bin/env bash

cd /opt/galaxy/tools
sudo su ubuntu -c "git clone https://github.com/Sage-Bionetworks/SMC-Het-Challenge-Examples.git"
service docker restart
restart_galaxy