#This function graphically renders the game world.

from botocore.vendored import requests
from PIL import Image
from io import BytesIO
import boto3

s3resource = boto3.resource('s3')

def lambda_handler(event, context):
    	
	house1url = "https://s3.amazonaws.com/derffred/house1.png"
	food1url  = "https://s3.amazonaws.com/derffred/food1.png"
	food2url  = "https://s3.amazonaws.com/derffred/food2.png"
	toy1url   = "https://s3.amazonaws.com/derffred/toy1.png"
	toy2url   = "https://s3.amazonaws.com/derffred/toy2.png"
	toy3url   = "https://s3.amazonaws.com/derffred/toy3.png"
	cat1url   = "https://s3.amazonaws.com/derffred/cat1.png"
	cat2url   = "https://s3.amazonaws.com/derffred/cat2.png"
	cat3url   = "https://s3.amazonaws.com/derffred/cat3.png"
	cat4url   = "https://s3.amazonaws.com/derffred/cat4.png"
	cat5url   = "https://s3.amazonaws.com/derffred/cat5.png"

	house1response = requests.get(house1url)
	food1response = requests.get(food1url)
	food2response = requests.get(food2url)
	toy1response = requests.get(toy1url)
	toy2response = requests.get(toy2url)
	toy3response = requests.get(toy3url)
	cat1response = requests.get(cat1url)
	cat2response = requests.get(cat2url)
	cat3response = requests.get(cat3url)
	cat4response = requests.get(cat4url)
	cat5response = requests.get(cat5url)

	mainimage = Image.open(BytesIO(house1response.content))
	imgfood1 =  Image.open(BytesIO(food1response.content))  
	imgfood2 =  Image.open(BytesIO(food2response.content))
	imgtoy1  =  Image.open(BytesIO(toy1response.content))
	imgtoy2  =  Image.open(BytesIO(toy2response.content))
	imgtoy3  =  Image.open(BytesIO(toy3response.content))
	imgcat1  =  Image.open(BytesIO(cat1response.content))
	imgcat2  =  Image.open(BytesIO(cat2response.content))
	imgcat3  =  Image.open(BytesIO(cat3response.content))
	imgcat4  =  Image.open(BytesIO(cat4response.content))
	imgcat5  =  Image.open(BytesIO(cat5response.content))

	#event = {"food1": True,"food2": True,"toy1": True,"toy2": True,"toy3": False,"cat1": True,"cat2": False,"cat3": True,"cat4": False,"cat5": True}

	if event['food1']:
		mainimage.paste(imgfood1, (0, 0), imgfood1)
	if event['food2']:
		mainimage.paste(imgfood2, (0, 0), imgfood2)
	if event['toy1']:
		mainimage.paste(imgtoy1,  (0, 0), imgtoy1)
	if event['toy2']:
		mainimage.paste(imgtoy2,  (0, 0), imgtoy2)
	if event['toy3']:
		mainimage.paste(imgtoy3,  (0, 0), imgtoy3)
	if event['cat1']:
		mainimage.paste(imgcat1,  (0, 0), imgcat1)
	if event['cat2']:
		mainimage.paste(imgcat2,  (0, 0), imgcat2)
	if event['cat3']:
		mainimage.paste(imgcat3,  (0, 0), imgcat3)
	if event['cat4']:
		mainimage.paste(imgcat4,  (0, 0), imgcat4)
	if event['cat5']:
		mainimage.paste(imgcat5,  (0, 0), imgcat5)
	
	mainimage.save('/tmp/tempfile.png')
	s3resource.Bucket('derffred').upload_file('/tmp/tempfile.png','worldview.png', ExtraArgs={'ACL':'public-read'})
		
	return event