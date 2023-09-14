create a kuber netes cluster on either of the platform of your choice. Example:a
- Rancher desktop
- Docker Desktop
- AWS EKS etc

I used Docker Desktop for this POC.

Now apply minio.yaml using kubectl: (I have setup k as an alias for kubectl)
>k apply -f minio.yaml

This will create a new namespace called minio-ns and will create a deployment and a NodePort service inside it:
>k get deploy -n minio-ns
>k get pods -n minio-ns
>k get svc -n minio-ns

while checking service, note down the two nodePorts corresponding to mino pod ports 9090(31072 in my case) and 9000(31074 in my case).

Use the NodePort corresponding to pod port 9090 to access Minio GUI on localhost:
http://localhost:31072/

Generate access-key and secret-key using this GUI in browser and use them in minio_client.py to access the hosted minio.

We will be using "localhost:31074" as API endpoint in our minio client written in python code(note that I have used the NodePort corresponding to API port i.e 9000):
localhost:31074

Install python minio module in case not present:
>pip install minio

Now we can use out minio client to access minio to create bucket, upload file, download file, list buckets etc.

We can also exec into the minio pod and check the "data" folder(which we had setup in minio.yaml)
>k exec -it -n minio-dev minio-598b59589-vwp26 -- /bin/bash
>ls
>cd data
ls

it will have all our buckets and corresponding objects within them