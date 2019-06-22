# This fuction is not yet implemented.
# This function will clear cats and food from the game world after a period of time.

import boto3

dynamoresource=boto3.resource('dynamodb')
table=dynamoresource.Table('switchboard')

#response = table.get_item(Key={'switch':'cat1'})
#subresponse = response['Item']
#print (subresponse)
#print (subresponse['status'])

table.put_item(Item={'switch':'food1','status':False})
table.put_item(Item={'switch':'food2','status':False})
table.put_item(Item={'switch':'toy1','status':False})
table.put_item(Item={'switch':'toy2','status':False})
table.put_item(Item={'switch':'toy3','status':False})
table.put_item(Item={'switch':'cat1','status':False})
table.put_item(Item={'switch':'cat2','status':False})
table.put_item(Item={'switch':'cat3','status':False})
table.put_item(Item={'switch':'cat4','status':False})
table.put_item(Item={'switch':'cat1','status':False})

#response = table.get_item(Key={'switch':'cat5'})

# table.put_item(Item={'Name':'BoYo','Age':'Baby'})