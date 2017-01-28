#!/usr/bin/env bash

source ./cluster.rc

killall -9 kubectl
gcloud container clusters delete ${CLUSTER_NAME} -z ${COMPUTE_ZONE}
gcloud compute disks delete --zone=${COMPUTE_ZONE} galaxy-data