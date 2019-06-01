# This function checks for input from the user.
# Users add food and toys to the game world through a DynamoDB table named switchboard.
# Changes at the switchboard are brought into a JSON string that is maintained by the state machine.
# The main purpose of this function is to bring front end requests by the user into the application's back end step function.


def lambda_handler(event, context):

    import boto3

    dynamoresource=boto3.resource('dynamodb')
    table=dynamoresource.Table('switchboard')

    response = table.get_item(Key={'switch':'food1'})
    subresponse = response['Item']
    f1 = (subresponse['status'])
    event['food1'] = f1

    response = table.get_item(Key={'switch':'food2'})
    subresponse = response['Item']
    f2 = (subresponse['status'])
    event['food2'] = f2
    
    response = table.get_item(Key={'switch':'toy1'})
    subresponse = response['Item']
    t1 = (subresponse['status'])
    event['toy1'] = t1
    
    response = table.get_item(Key={'switch':'toy2'})
    subresponse = response['Item']
    t2 = (subresponse['status'])
    event['toy2'] = t2
    
    response = table.get_item(Key={'switch':'toy3'})
    subresponse = response['Item']
    t3 = (subresponse['status'])
    event['toy3'] = t3

    response = table.get_item(Key={'switch':'cat1'})
    subresponse = response['Item']
    c1 = (subresponse['status'])
    event['cat1'] = c1
    
    response = table.get_item(Key={'switch':'cat2'})
    subresponse = response['Item']
    c2 = (subresponse['status'])
    event['cat2'] = c2
    
    response = table.get_item(Key={'switch':'cat3'})
    subresponse = response['Item']
    c3 = (subresponse['status'])
    event['cat3'] = c3
    
    response = table.get_item(Key={'switch':'cat4'})
    subresponse = response['Item']
    c4 = (subresponse['status'])
    event['cat4'] = c4

    response = table.get_item(Key={'switch':'cat5'})
    subresponse = response['Item']
    c5 = (subresponse['status'])
    event['cat5'] = c5

    print (f1,f2,t1,t2,t3,c1,c2,c3,c4,c5)
   
    return event
