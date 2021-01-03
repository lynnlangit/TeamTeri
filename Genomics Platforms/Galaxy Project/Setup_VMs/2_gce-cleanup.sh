#!/usr/bin/env bash

source ./0_cli.rc

# ------------------- CLEAN UP  -----------------------

echo "Delete firewall rule"
gcloud compute firewall-rules delete --quiet --project ${PROJECT} galaxy-allow-http &

echo "Deleting VM image..."
gcloud compute images delete --quiet --project ${PROJECT} ${TEAMTERI_IMAGE} &

echo "Deleting VM instances..."
gcloud compute instances delete --quiet ${GCLOUD_ARGS} ${VANILLA_INSTANCE} ${TOOLS_INSTANCE} &

echo "Waiting for gcloud to delete resources..."
wait
