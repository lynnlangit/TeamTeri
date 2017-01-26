#!/bin/bash

source ./cli.rc

# ---------------STARTING WITH GOOGLE CLOUD: STEP 0------------
echo "authenticate to GCP from your working directory via Terminal"
echo "will not launch if ${ACCOUNT} already has credentials"

gcloud auth login ${ACCOUNT} --brief

CLIENT_DISKS=`for i in $(seq 1 ${NUM_AS_CLIENTS}); do echo galaxy-persistent-disk-${i}; done`




# 1a. CREATE NETWORK / FIREWALL RULES
# //TODO - Create non-default network, add firewall rules to allow http/https traffic (to reach Galaxy)
# gcloud compute networks create...
# gcloud compute firewall-rules create...

# 1b. CREATE IMAGE to be used as a basis for your GCE instance (includes Galaxy install)
/bin/echo "Creating client image, please wait..."
#gcloud compute images create ${GCLOUD_ARGS}  \
#     --tags "Galaxy_client" --image ${TEAMTERI_IMAGE} \
#     --source-uri "galaxyproject_images/planemo_machine_smc.06.image.tar.gz"
gcloud compute images create ${TEAMTERI_IMAGE} \
    --description="Galaxy_client" \
    --source-uri="http://storage.googleapis.com/galaxyproject_images/planemo_machine_smc.06.image.tar.gz"

/bin/echo " galaxy GCE / VM image created..."

# 2a. CREATE CLIENT VMS & DISKS
/bin/echo "Creating client instances, please wait..."
gcloud compute instances create ${GCLOUD_ARGS} ${CLIENT_INSTANCES} \
    --machine-type ${CLIENT_INSTANCE_TYPE} --tags "galaxy-client" \
    --image ${TEAMTERI_IMAGE} --image-project ${PROJECT} \
    --boot-disk-size ${BOOT_DISK_SIZE}

# 2b. SETUP PERSISTENT DISKS (optional)
if [ ${USE_PERSISTENT_DISK} -eq 1 ]
then
    /bin/echo "Creating persistent disks..."
    gcloud compute disks create ${GCLOUD_ARGS} ${CLIENT_DISKS} --size "300GB"
    for i in $(seq 1 ${NUM_AS_CLIENTS}); do
        /bin/echo -n "  attaching galaxy-persistent-disk-$i to galaxy-client-$i:"
        gcloud compute instances ${GCLOUD_ARGS} attach-disk galaxy-client-${i} --disk galaxy-persistent-disk-${i}
    done
fi
/bin/echo " persistent disks created..."

# 3. CONNECT TO GALAXY on your GCE VM ('hello-gene')
# - Edit your VM to allow http/https traffic on the network for that VM (click in the GCP console)
#
# - Find the public IP of 'hello-gene', open http://<public ip of 'hello-gene'>, you should see Galaxy in your browser
# - Galaxy login is Username: planemo and Password: planemo
