# Installation - creates Galaxy instances on GCP Virtual Machine(s)

* **EDIT the 0_cli.rc file ** to add your email and project information 
* **REVIEW the default values ** for other variables in the same file

# Scripts
* **RUN `bash 0_cli.rc`** contains the configuration files for deploying galaxy on GCE.
* **RUN `bash 1_gce-standup.sh`** run this bash script to create one instance with default settings and one instance that uses a boot script to add some additional tools.
* **RUN `bash 2_gce-cleanup.sh`** run this bash script to cleanup the instances
* **READ use-galaxy-tool.md** describes how to do a simple test in Galaxy once the instances are created.
* **USE boot.sh** used when standing up instances to pre-install the extra Galaxy tools. 

# Galaxy access
* Scroll up to the top of the 'Compute Engine' GCP console and then click on the 'External IP' link to connect
* Log in as with username of 'admin' and password of 'admin' to connect to your Galaxy instance
