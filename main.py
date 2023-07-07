# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import base64
import boto3
import os
from botocore.exceptions import NoCredentialsError

BUCKET_NAME = 'fei-test1'
S3_REGION = 'us-west-1'
S3_ACCESSKEY_ID = 'AKIAQ2AEB2ZG4XTZXKWK'
S3_SECRET_ACCESS_KEY = os.environ['S3_SECRET_ACCESS_KEY']


def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3',
                      region_name=S3_REGION,
                      aws_access_key_id=S3_ACCESSKEY_ID,
                      aws_secret_access_key=S3_SECRET_ACCESS_KEY)
    try:
        s3.upload_file(local_file, BUCKET_NAME, s3_file)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': s3_file
            },
            ExpiresIn=24 * 3600
        )

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    upload_to_aws('./Recording.m4a', 'Recording.m4a')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
