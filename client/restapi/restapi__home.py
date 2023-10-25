# Import
import json
import requests


# Endpoint for the REST API
Endpoint = "http://localhost:8000/"


# Send a get request and store the data
data = requests.get(Endpoint).json()
data = json.dumps(data, indent=4)


# Print the data
print(data)
