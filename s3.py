import boto3

# Create an S3 client
s3 = boto3.client('s3')

def create_bucket(name):
    s3.create_bucket(Bucket=name)


def list_bucket():
    res = s3.list_buckets()
    return res
# Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')

# filename = 'hi.txt'
# bucket_name = 'bucketnodetest1'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
def upload(filename,bucket_name):
    s3.upload_file(filename, bucket_name, filename)

def download(filename,bucket_name):
    s3.download_file( bucket_name, filename, filename)
