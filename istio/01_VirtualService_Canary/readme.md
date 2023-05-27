# Use Killercoda istio playground:

# Add a namespace label to instruct Istio to automatically inject Envoy sidecar proxies when you deploy your application later:
>kubectl label namespace default istio-injection=enabled

# Either create your own docker images for two different apps by using the dockerfiles OR use the below images in your projects:
>docker build -t nikk007/app1 -f Dockerfile1 .
>docker build -t nikk007/app2 -f Dockerfile2 .

>docker login
>docker push nikk007/app1
>docker push nikk007/app2

# Create deployments:
>k apply -f deploy.yaml

# Now test the service to verify that both deployments are hit randomly(mostly in 50-50 ratio)
> while true; do curl localhost:30080; sleep .5; done

>k apply -f istio-rules.yaml

# we can see that we have "istio-ingressgateway" service of type Loadbalancer
>k get all -n istio-system

# convert it to type NodePort so that we can access it locally
>k edit svc istio-ingressgateway -n istio-system

# check services in istio-system namespace. In my case, nodeport 32147 was being used to direct to port 80. Now we can verify that we hit app2 90% of the times and app1 10% of the times(as specified in our istio VirtualService)
>while true; do curl localhost:32147; sleep .5; done

# we can change the percentages in istio-rules.yaml and reapply this yaml and then again check the results




