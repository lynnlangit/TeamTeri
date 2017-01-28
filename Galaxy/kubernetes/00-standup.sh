#!/usr/bin/env bash

source ./cluster.rc

gcloud config set core/project ${PROJECT_ID}
gcloud config set compute/zone ${COMPUTE_ZONE}
gcloud container clusters create ${CLUSTER_NAME}
gcloud container clusters get-credentials ${CLUSTER_NAME} --zone ${COMPUTE_ZONE} --project ${PROJECT_ID}

