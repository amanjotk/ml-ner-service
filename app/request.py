import requests
import json

url = 'http://127.0.0.1:8000/predict'

data = {"text": "Jack and Jill went up the hill"}
r = requests.post(url, json=json.dumps(data))
print(r.json())
