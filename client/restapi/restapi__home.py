# Import
import json
import requests


# Endpoint for the REST API
endpoint = "http://localhost:8000/"


# Send a get request and store the data
data = requests.get(endpoint).json()
data = json.dumps(data, indent=4)


# Print the data
print(data)
