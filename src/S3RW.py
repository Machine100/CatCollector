from PIL import Image
import requests
from io import BytesIO

url = "https://s3.amazonaws.com/derffred/house1.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))