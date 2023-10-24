install argoCD on local k8s cluster. I am using docker-desktop for a local cluster:

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

Setup jenkins on this cluster:
- k apply jenkins-setup.yaml

For retreiving Jenkins password:
k exec -it jenkins-68fdd84594-hkpmt -- cat /var/jenkins_home/secrets/initialAdminPassword

Then install github, pipeline plugins during Jenkins initialization.
==============================================================================

We will have two github repos: repo-a and repo-b.
repo-a will have our python app code, requirements.txt and Dockerfile.
repo-b will have the deployemnt and service yamls and this repo will be used for gitops.

===============================================================================

To setup Python app, inside python-app folder(this will be done via Jenkins):

docker build -t nikk007/mypython-app:latest .
docker push nikk007/mypython-app:latest

===============================================================================

Now we can setup github webhook so as to trigger Jenkins once the changes are pushed to the app's git repo i,e repo-a.
Then Jenkins will build the image and tag it with the current time in ms.
Then this tag can be sent to some Lambda function which will check if a branch with the same name exists on repo-b and create a branch with the same name there. THen send the new deployment with updated image name to the git repo.
A push in repo-b will be seen by the argoCD app in our kubernetes cluster and it will make the changes in the app deployed on the cluster.
================================================================================









