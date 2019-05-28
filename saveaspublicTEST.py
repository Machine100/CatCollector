#This function graphically renders the game world.


import boto3

s3resource = boto3.resource('s3')

s3resource.Bucket('derffred').upload_file('test.txt','outputdestinationtest.png', ExtraArgs={'ACL':'public-read'})
		
