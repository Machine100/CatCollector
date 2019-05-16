
import boto3

dynamoresource=boto3.resource('dynamodb')
table=dynamoresource.Table('switchboard')

response = table.get_item(Key={'switch':'food1'})
subresponse = response['Item']
f1 = (subresponse['status'])

response = table.get_item(Key={'switch':'food2'})
subresponse = response['Item']
f2 = (subresponse['status'])

response = table.get_item(Key={'switch':'toy1'})
subresponse = response['Item']
t1 = (subresponse['status'])

response = table.get_item(Key={'switch':'toy2'})
subresponse = response['Item']
t2 = (subresponse['status'])

response = table.get_item(Key={'switch':'toy3'})
subresponse = response['Item']
t3 = (subresponse['status'])

response = table.get_item(Key={'switch':'cat1'})
subresponse = response['Item']
c1 = (subresponse['status'])

response = table.get_item(Key={'switch':'cat2'})
subresponse = response['Item']
c2 = (subresponse['status'])

response = table.get_item(Key={'switch':'cat3'})
subresponse = response['Item']
c3 = (subresponse['status'])

response = table.get_item(Key={'switch':'cat4'})
subresponse = response['Item']
c4 = (subresponse['status'])

response = table.get_item(Key={'switch':'cat5'})
subresponse = response['Item']
c5 = (subresponse['status'])

print (f1,f2,t1,t2,t3,c1,c2,c3,c4,c5)


# table.put_item(Item={'Name':'BoYo','Age':'Baby'})


