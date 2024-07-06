import boto3
from dotenv import load_dotenv
import os
from botocore.exceptions import NoCredentialsError

load_dotenv()

def create_bucket(bucket_name):
    try:
        s3_service.create_bucket(
            Bucket=bucket_name
        )
        print("Bucket created")
        return True
    except NoCredentialsError:
        print("Credentials not available or incorrect")
        return False
    except Exception as e:
        print(f"General error: {e}")
        return False

def upload_files(local_file_path, bucket_name, file_cloud_name):
    try:
        s3_service.upload_file(local_file_path, bucket_name, file_cloud_name)
        print("Upload completed")
        return True
    except FileNotFoundError:
        print(f"The file {local_file_path} was not found.")
        return False
    except NoCredentialsError:
        print("Credentials not available.")
        return False
    except Exception as e:
        print(f"Error during upload: {e}")
        return False


key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token = os.getenv("AWS_SESSION_TOKEN")
region_name = os.getenv("REGION_NAME")

s3_service = boto3.client(
    's3',
    aws_access_key_id = key_id,
    aws_secret_access_key = secret_key,
    aws_session_token = session_token,
    region_name = region_name
)

bucket_name = "akaz-upload-csv-test-bucket"
local_file_path = "data/data_sales.csv"
file_cloud_name = "input/data_sales.csv"

create_bucket(bucket_name)
upload_files(local_file_path, bucket_name, file_cloud_name)
