create two kind clusters(refer kind cluster setup poc):
kind create cluster --config kind-config-cluster1.yaml --name cluster1
kind create cluster --config kind-config-cluster1.yaml --name cluster2

k config current-context
k config set-context kind-cluster1

k apply -f myapp1.yaml

Install Velero CLI:

# Download the Velero binary
wget https://github.com/vmware-tanzu/velero/releases/download/v1.12.4/velero-v1.12.4-linux-amd64.tar.gz

# Extract the binary
tar -xvf velero-v1.7.0-linux-amd64.tar.gz

# Move the binary to a directory in your PATH
sudo mv velero-v1.12.4-linux-amd64/velero /usr/local/bin/

# Verify the installation
velero version
----------------------------------------

setup minio deployment:

k apply -f minio.yaml

# Use the NodePort corresponding to pod port 9090 to access Minio GUI on localhost

to create a bucket named "mybucket" in minio(pod) by executing a command inside minio bucket:
k exec -it minio-7d9c6f497-wlgcr -n minio-ns -- sh -c "mkdir /data/mybucket"

cat <<EOF>> minio.credentials
[default]
aws_access_key_id=minio
aws_secret_access_key=minio123
EOF

echo "AWS_ACCESS_KEY_ID=qGeIRVGqP5Vgmj23qKcj" > minio.credentials
echo "AWS_SECRET_ACCESS_KEY=d7vNzZkTQiZaBHshVAVYIMZtOx6q1AkoL44Nco2D" >> minio.credentials

---------------------------------------------------

Install Velero Server aws plugin:
velero install \
   --provider aws \
   --uploader-type=restic \
   --plugins velero/velero-plugin-for-aws:v1.9.0 \
   --bucket mybucket \
   --secret-file /mnt/c/nikk/devopsprojects/kubernetes/08-velero-minio-backup/minio.credentials \
   --backup-location-config region=minio,s3ForcePathStyle=true,s3Url=http://10.99.241.71:9000,insecureSkipTLSVerify=true


velero backup create myfirstbackup
velero backup describe myfirstbackup --details
velero backup logs myfirstbackup
velero get backups
velero delete backup myfirstbackup







