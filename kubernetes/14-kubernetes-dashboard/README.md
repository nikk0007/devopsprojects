to deploy complete kubernetes dashboard, we can use the following:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml

But, in case we dont want to use this yaml from the internet and want to save images on own registry, THEN we need to find out the images required.

Complete yaml is downloaded into dashboard-complete.yaml file. Now we will try to identify the individial images in it.

kubernetesui/dashboard:v2.7.0
kubernetesui/metrics-scraper:v1.0.8











