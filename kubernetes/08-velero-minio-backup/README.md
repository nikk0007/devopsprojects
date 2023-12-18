create two kind clusters(refer kind cluster setup poc):
kind create cluster --config kind-config-cluster1.yaml --name cluster1
kind create cluster --config kind-config-cluster1.yaml --name cluster2

k config current-context
k config set-context kind-cluster1

k apply -f myapp1.yaml

Install Velero CLI:

# Download the Velero binary
wget https://github.com/vmware-tanzu/velero/releases/download/v1.7.0/velero-v1.7.0-linux-amd64.tar.gz

# Extract the binary
tar -xvf velero-v1.7.0-linux-amd64.tar.gz

# Move the binary to a directory in your PATH
sudo mv velero-v1.7.0-linux-amd64/velero /usr/local/bin/

# Verify the installation
velero version
----------------------------------------

setup minio deployment:

k apply -f minio.yaml

to create a bucket named "mybucket" in minio(pod) by executing a command inside minio bucket:
k exec -it minio-7d9c6f497-wlgcr -n minio-ns -- sh -c "mkdir /data/mybucket"

velero create backup-location my-minio-backup --provider aws --bucket mybucket --access-key-id D2EzDvezbhUfaEDVWVla--secret-access-key JU7HMrUCvz8yAxKnpvTuPZbEVNgafQxaWzHk2XGw --config ./minio-config

velero create backup-location my-minio-backup --provider aws --bucket mybucket \
  --config endpoint=http://localhost:32058,publicUrl=http://localhost:32058,s3ForcePathStyle="true" \
  --access-key-id D2EzDvezbhUfaEDVWVla --secret-access-key JU7HMrUCvz8yAxKnpvTuPZbEVNgafQxaWzHk2XGw



cat <<EOF>> minio.credentials
[default]
aws_access_key_id=minio
aws_secret_access_key=minio123
EOF

echo "AWS_ACCESS_KEY_ID=D2EzDvezbhUfaEDVWVla" > minio.credentials
echo "AWS_SECRET_ACCESS_KEY=JU7HMrUCvz8yAxKnpvTuPZbEVNgafQxaWzHk2XGw" >> minio.credentials

velero create backup-location my-minio-backup --provider aws --bucket mybucket --config region=minio,s3ForcePathStyle="true",s3Url=http://localhost:32058 --secret-file=minio.credentials

export AWS_ACCESS_KEY_ID=D2EzDvezbhUfaEDVWVla
export AWS_SECRET_ACCESS_KEY=JU7HMrUCvz8yAxKnpvTuPZbEVNgafQxaWzHk2XGw

velero create backup-location my-minio-backup --provider aws --bucket mybucket \
  --config region=minio,s3ForcePathStyle="true",s3Url=http://localhost:32058

Install Velero Server:
velero install \
   --provider aws \
   --use-restic \
   --plugins velero/velero-plugin-for-aws:v1.7.0 \
   --bucket mybucket \
   --secret-file ./minio.credentials \
   --backup-location-config region=minio,s3ForcePathStyle=true,s3Url=http://localhost:32058

velero backup create myfirstbackup
velero backup describe myfirstbackup --details
velero backup logs myfirstbackup







