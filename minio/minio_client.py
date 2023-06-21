from minio import Minio

# Initialize the Minio client
minio_client = Minio(
    "localhost:31074",
    access_key="<YOUR AWS ACCESS KEY>",
    secret_key="<YOUR AWS SECRET KEY>",
    secure=False  # Set it to True if you're using HTTPS
)

# Create a new bucket
def create_bucket(bucket_name):
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
    else:
        print(f"Bucket '{bucket_name}' already exists.")

# Upload a file to a bucket
def upload_file(bucket_name, file_path, object_name):
    minio_client.fput_object(bucket_name, object_name, file_path)
    print(f"File '{file_path}' uploaded as '{object_name}'.")

# Download a file from a bucket
def download_file(bucket_name, object_name, file_path):
    minio_client.fget_object(bucket_name, object_name, file_path)
    print(f"File '{object_name}' downloaded to '{file_path}'.")

# List objects in a bucket
def list_objects(bucket_name):
    objects = minio_client.list_objects(bucket_name, recursive=True)
    for obj in objects:
        print(obj.object_name)

# Example usage
if __name__ == "__main__":
    bucket_name = "my-bucket"
    object_name = "my-object"
    file_path = "sample-file.txt"

    create_bucket(bucket_name)
    upload_file(bucket_name, file_path, object_name)
    download_file(bucket_name, object_name, "downloads/downloaded_file.txt")
    list_objects(bucket_name)
