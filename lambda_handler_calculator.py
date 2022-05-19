from __future__ import print_function

import json

print('Loading function')


def lambda_handler(event, context):
    return {
        "status": 200,
        "event": event
    }
