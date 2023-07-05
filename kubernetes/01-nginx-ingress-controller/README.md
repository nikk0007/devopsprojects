In this POC, I will be using Docker Desktop for creating a kubernetes cluster on windows machine. I will use WSL2 Ubuntu for running commands.

We will create two deployments and two corresponding services. Then we will use Ingress controller to route to these services based on the path we privide in the url.

Deploy the Microservices:
- k create deployment app1 --image=gcr.io/google-samples/hello-app:1.0
- k create deployment app2 --image=gcr.io/google-samples/hello-app:2.0

- k expose app1 --type=NodePort --target-port=8080
- k expose app2 --type=NodePort --target-port=8080

- k get svc

Now we can test that we are able to access both of these services on browser using:
- localhost:<NodePort>
==========================================================

Deploy Nginx Ingress Controller

Create a namespace for the Ingress Controller: Open wsl2 ubuntu and run the following command:

- kubectl create namespace ingress-nginx

Deploy the Nginx Ingress Controller: Run the following command to deploy the Nginx Ingress Controller:

- kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.4/deploy/static/provider/cloud/deploy.yaml -n ingress-nginx

Verify the deployment: Run the following command to check the status of the Ingress Controller deployment:

- kubectl get pods -n ingress-nginx
=============================================================

Then we will apply the ingress resource i.e ingress.yaml which has rules to send requests with myapp1path to app1 service and myapp2path to app2 service. We can check this in browser:
- localhost/myapp1path
- localhost/myapp2path

You can also check nginx-controller logs as you access the above urls:
- k logs <ingress-nginx-controller-POD_NAME> -n ingress-nginx
==============================================================

Here: nginx ingress Controller effectively reads the ingress rules from our kubernetes ingress resourse and updates its own configuration accordingly.
===============================================================

