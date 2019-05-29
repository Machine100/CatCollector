import json
import boto3

def lambda_handler(event, context):

    dynamoresource=boto3.resource('dynamodb')
    table=dynamoresource.Table('switchboard')

    table.put_item(Item={'switch':'food1','status':True})

    return {
        'statusCode': 200,
        'body': json.dumps('You hit my endpoint')
    }
