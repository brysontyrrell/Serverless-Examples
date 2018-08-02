import json
import time


def lambda_handler(event, context):

    for record in event['Records']:
        body = json.loads(record['body'])
        print(f'SQS message content: {body}')
        time.sleep(2)

    return {}
