after installing docker-desktop, set the kubeconfig path:
export KUBECONFIG=/home/nikk/.kube/config

to change storage class without losing data.

So we have say, 2 storage classes: sc1 and sc2 which will be used by pvc1 and pvc2 respectively inside the deployment volumes.

Here we will apply sc1 and then pvc1 anf then apply the nginx deployment where we have mounted the pvc1 at /usr/share/nginx/html/
We also create a nodeport svc to expose the nginx deployment.
Now we exec into the pod and put some message(to be displayed in browser) at path: /usr/share/nginx/html/index.html

here we are considering index.html as our DATA to be preserved while changing the sc.

No we apply sc2 nd pvc2 and edit the deployment to mount pvc2 on some path(say, /tmp/new) ==> pod will be recreated and it will have pvc1 and pvc2 both mounted.

Now we copy the data(index.html) from pvc1 path to pvc2 path using the below command:
cp -r /usr/share/nginx/html/* /tmp/new/

this will effectively create a copy of pvc1 into pvc2.
Now we again edit the deployment to delete the pvc1 volume and volumemount, and point pvc2 to the path /usr/share/nginx/html/.
New pod will be created which wont have pvc1. Now pvc1 and sc1 both can be deleted safely.









