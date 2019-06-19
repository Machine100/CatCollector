import boto3

#dynamoresource=boto3.resource('dynamodb')
stepfunctionclient = boto3.client('stepfunctions')

response = stepfunctionclient.start_execution(
    stateMachineArn='arn:aws:states:us-east-1:980965586942:stateMachine:CatCollectorStepFunction',
    )