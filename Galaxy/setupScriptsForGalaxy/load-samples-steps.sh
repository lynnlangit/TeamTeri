#!/usr/bin/env bash
# SSH to GCE / Galaxy instance

# change to galaxy user
sudo su ubuntu 

# change to galaxy directory
cd /opt/galaxy/tools/

# clone sample tools
git clone https://github.com/Sage-Bionetworks/SMC-het-challenge-examples.git

# restart galaxy to load new tools
restart_galaxy

#open code ide (log in with your email)
<public ip address/ide/