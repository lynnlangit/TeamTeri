#!/bin/bash

# ---------------Load example Galaxy Tools------------
# Using the GCP (GCE) console, click the 'SSH' button to open an SSH shell

sudo su ubuntu
cd /opt/galaxy/tools
git clone https://github.com/Sage-Bionetworks/SMC-Het-Challenge-Examples.git
# cd SMC-Het-Challenge-Examples

sudo service docker restart
restart_galaxy

# import data (within Galaxy) using the 'Data' link --> import history
# test the tools
# use this file In the 'VCF file' field select 'Tumour1.mutect.vcf'
# evalate results using the Evaluator Tool in the left hand tool panel