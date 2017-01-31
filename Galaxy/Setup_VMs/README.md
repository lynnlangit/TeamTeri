# Installation - creates Galaxy instances on GCP Virtual Machine(s)

* Add your email and project to the 0_cli.rc file
* Review the default values for other variables in the same file

# Files
* **0_cli.rc** contains the configuration files for deploying galaxy on GCE.
* **1_gce-standup.sh** run this bash script to create one instance with default settings and one instance that uses a boot script to add some additional tools.
* **2_gce-cleanup.sh** run this bash script to cleanup the instances
* **use-galaxy-tool.md** describes how to do a simple test in Galaxy once the instances are created.
* **boot.sh** used when standing up instances to pre-install the extra tools. 

# Notes
* After Galaxy instances launch, manually edit the GCE (VM) configuration to allow http access
* Click the 'edit' button in the 'Compute Engine' GCP console for your instance
* Scroll down to the 'Firewalls' section and click the box 'Allow HTTP' traffic
* Scroll to the bottom of the page and click the blue 'Save' button
* Scroll up to the top of the 'Compute Engine' GCP console and then click on the 'External IP' link to connect
* Log in as with username of 'admin' and password of 'admin' to connect to your Galaxy instance
