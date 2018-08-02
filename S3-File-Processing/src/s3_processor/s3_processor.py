import io
import json
import logging

import boto3
from botocore.vendored import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_file(bucket, key):
    logger.info("Downloading '%s' from S3 Bucket '%s'", key, bucket)
    bucket = boto3.resource('s3').Bucket(bucket)
    f_obj = io.BytesIO()
    try:
        bucket.download_fileobj(Key=key, Fileobj=f_obj)
    except:
        logger.error('The download failed!')
        raise
    else:
        logger.info('Download succeeded')
    return json.loads(f_obj.getvalue())


def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        data = get_file(bucket_name, object_key)

        # Perform file processing...
        requests.put(
            'https://my/service',
            data=json.dumps(data),
            headers={'Content-Type': 'application/json'}
        )

    return {}
