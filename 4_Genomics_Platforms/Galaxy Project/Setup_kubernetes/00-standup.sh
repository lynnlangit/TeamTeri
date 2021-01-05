#!/usr/bin/env bash

echo "Importing configuration from cluster.rc"
source ./cluster.rc

echo "Setting cli defaults..."
gcloud config set core/project ${PROJECT_ID}
gcloud config set compute/zone ${COMPUTE_ZONE}

echo "Starting cluster and creating external disk..."
gcloud container clusters create ${CLUSTER_NAME} &

gcloud compute disks create \
    --size=500GB \
    --zone=${COMPUTE_ZONE} \
    galaxy-export \
    &

echo "Waiting for cluster and disk to become available..."
wait

echo "Getting cluster credentials for kubectl..."
gcloud container clusters get-credentials ${CLUSTER_NAME} \
    --zone ${COMPUTE_ZONE} \
    --project ${PROJECT_ID}