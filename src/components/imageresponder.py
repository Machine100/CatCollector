import boto3
from botocore.vendored import requests
s3client = boto3.client('s3')

      
file = requests.get('https://picsum.photos/200')

print (type(file))