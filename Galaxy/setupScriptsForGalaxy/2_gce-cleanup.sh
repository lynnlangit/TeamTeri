#!/usr/bin/env bash

source ./0_cli.rc

# ------------------- CLEAN UP  -----------------------

echo "Delete firewall rule"
gcloud compute firewall-rules delete --project ${PROJECT} galaxy-allow-http

echo "Deleting VM image..."
gcloud compute images delete --project ${PROJECT} ${TEAMTERI_IMAGE}

echo "TODO: Detaching disks..."

echo "TODO: Deleting disks..."

echo "Deleting VM instances..."
gcloud compute instances delete --quiet ${GCLOUD_ARGS} ${CLIENT_INSTANCES}
