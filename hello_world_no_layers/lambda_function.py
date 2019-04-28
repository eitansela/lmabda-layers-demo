import json
import my_lambda_utils

def lambda_handler(event, context):
    
    my_lambda_utils.print_hello()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
