#!/bin/bash

echo "Importing configuration from cli.rc..."
source ./cli.rc

echo "authenticate to GCP from your working directory via Terminal"
echo "will not launch if ${ACCOUNT} already has credentials"
gcloud auth login ${ACCOUNT} --brief

echo "Creating firewall rule..."
gcloud compute firewall-rules create galaxy-allow-http --allow tcp:80 --target-tags ${CLIENT_TAG}

echo "Creating client image, please wait..."
gcloud compute images create ${TEAMTERI_IMAGE} \
    --description="Galaxy_client" \
    --source-uri="http://storage.googleapis.com/galaxyproject_images/planemo_machine_smc.06.image.tar.gz"

echo "Creating persistent disk image..."
gcloud compute disks create --size=500GB --zone=${ZONE} ${PERSISTENT_DISK}

echo "Creating client instances, please wait..."
gcloud compute instances create ${GCLOUD_ARGS} ${CLIENT_INSTANCES} \
    --machine-type ${CLIENT_INSTANCE_TYPE} \
    --tags ${CLIENT_TAG} \
    --image ${TEAMTERI_IMAGE} \
    --image-project ${PROJECT} \
    --boot-disk-size ${BOOT_DISK_SIZE} \
    --disk=name=${PERSISTENT_DISK},device-name=${PERSISTENT_DISK} \
    --metadata-from-file startup-script=boot.sh

# See https://cloud.google.com/compute/docs/disks/add-persistent-disk for what todo with the disk.

#CLIENT_DISKS=`for i in $(seq 1 ${NUM_AS_CLIENTS}); do echo galaxy-persistent-disk-${i}; done`
## 2b. SETUP PERSISTENT DISKS (optional)
#if [ ${USE_PERSISTENT_DISK} -eq 1 ]
#then
#    /bin/echo "Creating persistent disks..."
#    gcloud compute disks create ${GCLOUD_ARGS} ${CLIENT_DISKS} --size "300GB"
#    for i in $(seq 1 ${NUM_AS_CLIENTS}); do
#        /bin/echo -n "  attaching galaxy-persistent-disk-$i to galaxy-client-$i:"
#        gcloud compute instances ${GCLOUD_ARGS} attach-disk galaxy-client-${i} --disk galaxy-persistent-disk-${i}
#    done
#fi
#/bin/echo " persistent disks created..."