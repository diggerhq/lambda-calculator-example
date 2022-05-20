from __future__ import print_function

import json

print('Loading function')


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": event
    }
