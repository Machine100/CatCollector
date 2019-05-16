
import boto3

dynamoresource=boto3.resource('dynamodb')
table=dynamoresource.Table('switchboard')

#set item to true
#table.put_item(Item={'switch':'cat1','status':True})

response = table.get_item(Key={'switch':'cat1'})
subresponse = response['Item']
print (subresponse)
print (subresponse['status'])

#if response []:


#set item to false
table.put_item(Item={'switch':'cat1','status':False})
response = table.get_item(Key={'switch':'cat1'})
print (response)



# table.put_item(Item={'Name':'BoYo','Age':'Baby'})


