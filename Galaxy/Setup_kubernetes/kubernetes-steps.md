##Setup Galaxy Docker instance on GCP Kubernetes cluster

###Prepare and Run Scripts
* **UPDATE** `cluster.rc`, add your project name.
* **RUN** `bash 00-standup.sh`

###Deploy Galaxy to the cluster
After the cluster is up, then you can deploy Galaxy to your cluster with this command:
* **DEPLOY GALAXY** `bash kubectl apply -f primary-deployment.yaml`
NOTE: This command tells kubernetes to create the replication controller and service described in the YAML file.

###Monitor your cluster
To monitor progress of the deployment you create a proxy that allows access to the kubernetes UI.
* **MONITOR DEPLOYMENT** `bash kubectl proxy`
This command will print a message indicating that the proxy has started.  Wait for the cluster to be ready (green circle).

###Use Galaxy
Visit your cluster UI at this address:
* **VISIT CLUSTER** go to this address `http://localhost:8001/ui`

In the Kubernetes UI, click the "Services" link in the left hand menu, and then click the hyperlink there which will take you to the IP where Galaxy is running.
