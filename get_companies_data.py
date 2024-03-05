import os
import csv
from minio import Minio

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



# Iterate over the objects and filter CSV files
csv_lines = []

header_written = False

for obj in objects:
    if obj.object_name.endswith('.csv'):
        response = minio_client.get_object(bucket_name, obj.object_name)
        content = response.data.decode('utf-8').splitlines()
        
        reader = csv.reader(content)
        rows = list(reader)
        if not header_written:
            csv_lines.extend(rows)
            header_written = True
        else:
            csv_lines.extend(rows[1:])
        

with open('customers_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_lines)

print('job_done')