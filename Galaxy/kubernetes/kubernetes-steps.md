Update cluster.rc, add your project name.

Run `bash 00-standup.sh`

When the cluster is up you can deploy Galaxy with this command:

`kubectl apply -f primary-deployment.yaml`

This command tells kubernetes to create the recplication controller and service described in the YAML file.

Next you can monitor progress of the deployment by creating a proxy that allows access to the kubernetes UI.

`kubectl proxy`

This command will print a message indicating that the proxy has started.  Next, you can visit the cluster UI at this address:

http://localhost:8001/ui

In the UI, you can go to "Services" in the left hand menu, and then click the hyperlink there which will take you to the IP where Galaxy is running.