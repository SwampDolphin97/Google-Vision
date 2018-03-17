import os
import io
from google.cloud.vision import types
from google.cloud import vision
import pprint

def detect(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('What I have found')
	
    flag=0	
    for label in labels:
	print(label.description)
	
filename = raw_input("Enter filename:")
detect(filename)
