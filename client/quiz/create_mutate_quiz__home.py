# Import
import json
import requests


# Endpoint for the REST API
endpoint = "http://localhost:8000/quiz/"


session = requests.Session()


# Get the CSRF token
token_response = session.get(endpoint, verify=False)
csrf_token = token_response.cookies["csrftoken"]


# Declare the mutate
mutate = """
mutation {
    addCategory(name:"Cyber Security") {
        category {
            id
            name
        }
    }
}
"""


# Send a post request and store the data
data = session.post(
    endpoint, data={"query": mutate, "csrfmiddlewaretoken": csrf_token}
).json()
data = json.dumps(data, indent=4)


# Print the data
print(data)
