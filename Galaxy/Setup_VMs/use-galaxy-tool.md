# Load example Galaxy Tools

Use the GCP (GCE) console, click the 'SSH' button to open an SSH shell

```
sudo su ubuntu
cd /opt/galaxy/tools
git clone https://github.com/Sage-Bionetworks/SMC-Het-Challenge-Examples.git

sudo service docker restart
restart_galaxy
```

# Test example Galaxy Tools with Sample Data

* Import data (within Galaxy) using the 'Data' link --> import history
* Use this file in the 'VCF file' field select 'Tumour1.mutect.vcf'
* Click 'Execute' to run the tool - this can take up to 30 minutes to complete
* Evalate results using the Evaluator Tool (SMC-HeT Evaluator) in the left hand tool panel
* NOTE: The example is from this link - https://www.synapse.org/#!Synapse:syn2813581/wiki/303161
