import os
import csv
from minio import Minio

def download_most_recent_company_file():
    # Retrieve environment variables
    minio_root_user = os.environ.get('MINIO_ROOT_USER')
    minio_root_password = os.environ.get('MINIO_ROOT_PASSWORD')
    minio_host = 'localhost'
    minio_port = 9000

    # Create MinIO client
    minio_client = Minio(
        endpoint=f'{minio_host}:{minio_port}',
        access_key=minio_root_user,
        secret_key=minio_root_password,
        secure=False,
    )

    # Retrieve customer data
    bucket_name = 'companies'

    # List objects in the bucket
    objects = minio_client.list_objects(bucket_name, recursive=True)

    # Initialize variables to track the most recent file
    most_recent_file = None
    most_recent_date = None

    # Iterate over the objects and find the CSV file with the latest date
    for obj in objects:
        if obj.object_name.endswith('.csv'):
            # Get the filename
            filename = obj.object_name

            # Extract the date from the filename
            date_str = filename[:-4]  # Remove the '.csv' extension

            # Compare with the current most recent date
            if most_recent_date is None or date_str > most_recent_date:
                most_recent_file = filename
                most_recent_date = date_str

    # Download the most recent CSV file
    if most_recent_file:
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, most_recent_file)
        minio_client.fget_object(bucket_name, most_recent_file, file_path)
        return file_path
    else:
        return None
