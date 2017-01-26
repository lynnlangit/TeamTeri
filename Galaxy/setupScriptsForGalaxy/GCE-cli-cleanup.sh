#!/usr/bin/env bash

source ./cli.rc

# ------------------- CLEAN UP  -----------------------

# DELETE IMAGE
echo "Deleting VM image..."
gcloud compute images delete ${TEAMTERI_IMAGE}

# DELETE ALL INSTANCES
echo "Deleting VM instances..."
gcloud compute instances delete --quiet ${GCLOUD_ARGS} ${CLIENT_INSTANCES}

# DELETE DISKS (Optional - you may wish to save these disks for reuse with new VM instances)
if [ ${USE_PERSISTENT_DISK} -eq 1 ]
then
    /bin/echo "Detaching persistent disks..."
    for i in $(seq 1 ${NUM_AS_CLIENTS}); do
      /bin/echo -n "  galaxy-persistent-disk-$i"
      gcloud compute instances detach-disk ${GCLOUD_ARGS} galaxy-client-${i} --disk galaxy-persistent-disk-${i}
    done
    /bin/echo "  deleting disks..."
    gcloud compute disks delete ${GCLOUD_ARGS} ${CLIENT_DISKS} -q
fi
