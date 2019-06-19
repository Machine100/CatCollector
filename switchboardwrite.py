# This function is used for development.
# This function is not implemented in production.

import boto3

dynamoresource=boto3.resource('dynamodb')
table=dynamoresource.Table('switchboard')

response = table.get_item(Key={'switch':'cat1'})
#subresponse = response['Item']
#print (subresponse)
#print (subresponse['status']
)
#table.put_item(Item={'switch':'food1','status':True})
#table.put_item(Item={'switch':'food2','status':True})
#table.put_item(Item={'switch':'toy1','status':True})
#table.put_item(Item={'switch':'toy2','status':True})
#table.put_item(Item={'switch':'toy3','status':True})
#table.put_item(Item={'switch':'cat1','status':True})
#table.put_item(Item={'switch':'cat2','status':True})
#table.put_item(Item={'switch':'cat3','status':True})
#table.put_item(Item={'switch':'cat4','status':True})
#table.put_item(Item={'switch':'cat1','status':True})

#response = table.get_item(Key={'switch':'cat5'})

# table.put_item(Item={'Name':'BoYo','Age':'Baby'})


