# Installation - creates Galaxy instances on GCP Virtual Machine(s)

* Add your email and project to the 0_cli.rc file
* Review the default values for other variables in the same file

# Files
* **0_cli.rc** contains the configuration files for deploying galaxy on GCE.
* **1_1a_gce-standup.sh.rc** run this script to get the default galaxy installation
* **1b_gce-standup_and_run_boot-script.sh** runs an additional script (boot.sh) during instance startup
* **2_gce-cleanup.sh** to cleanup the instances
* **add-galaxy-tools-and-use.sh** bash script; manually run this file inside a GCE instance
* **boot.sh** functionally same as the previous script and is run automatically by **1b** above 

# Notes
* After Galaxy instances launch, manually edit the GCE (VM) configuration to allow http access
* Click the 'edit' button in the 'Compute Engine' GCP console for your instance
* Scroll down to the 'Firewalls' section and click the box 'Allow HTTP' traffic
* Scroll to the bottom of the page and click the blue 'Save' button
* Scroll up to the top of the 'Compute Engine' GCP console and then click on the 'External IP' link to connect
* Log in as with username of 'admin' and password of 'admin' to connect to your Galaxy instance
