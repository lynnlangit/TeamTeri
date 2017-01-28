#!/usr/bin/env bash

source ./cluster.rc

gcloud compute disks create --size=500GB --zone=${COMPUTE_ZONE} galaxy-export