## Installation - creates Galaxy instances on GCP Virtual Machine(s)

### Prepare Scripts
* **EDIT your 0_cli.rc file** to add your email and project information 
* **REVIEW the default values** for other variables in the same file

### Run Scripts
* **RUN `bash 0_cli.rc`** contains the configuration files for deploying galaxy on GCE.
* **RUN `bash 1_gce-standup.sh`** run this bash script to create one instance with default settings and one instance that uses a boot script to add some additional tools.
* **RUN `bash 2_gce-cleanup.sh`** run this bash script to cleanup the instances
* **READ use-galaxy-tool.md** describes how to do a simple test in Galaxy once the instances are created.
* **USE boot.sh** used when standing up instances to pre-install the extra Galaxy tools. 

### Access Galaxy 
* **CLICK ON** the GCP console -> 'Compute Engine' link
* **CLICK ON** the 'External IP' link of your GCE instance to connect to Galaxy
* **LOGIN** to your Galaxy instance with the default username of 'admin' and password of 'admin' 
