import requests

API_URL = "https://b30yzz53beqp1cwp.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "image/png",
	"Content-Type": "application/json" 
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

output = query({
	"inputs": "Astronaut riding a horse",
	"parameters": {}
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(output))
