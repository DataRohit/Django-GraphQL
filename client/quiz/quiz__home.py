# Import
import json
import requests


# Endpoint for the REST API
endpoint = "http://localhost:8000/quiz/"


# Declare the query
query = """
query {
    allQuizzes(title: "code") {
        id
        title
        category {
            name
        }
        question {
            title
            answer {
                answerText
                isRight
            }
        }
    }
}
"""


# Send a get request and store the data
data = requests.get(endpoint, json={"query": query}).json()
data = json.dumps(data, indent=4)


# Print the data
print(data)
