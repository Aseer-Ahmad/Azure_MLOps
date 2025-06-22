import requests
import json
import os

scoring_uri = "http://3330f4fb-fea1-4497-b80a-ae9c8a25887c.eastus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = os.getenv("WS_ENDPOINT_KEY")

data = {
  "Inputs": {
    "data": [
      {
        "age": 0,
        "job": "technician",
        "marital": "married",
        "education": "basic.9y",
        "default": "no",
        "housing": "no",
        "loan": "yes",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "duration": 0,
        "campaign": 0,
        "pdays": 0,
        "previous": 0,
        "poutcome": "failure",
        "emp.var.rate": 0,
        "cons.price.idx": 0,
        "cons.conf.idx": 0,
        "euribor3m": 0,
        "nr.employed": 0
      },
            {
        "age": 33,
        "job": "admin.",
        "marital": "divorced",
        "education": "basic.9y",
        "default": "yes",
        "housing": "yes",
        "loan": "yes",
        "contact": "cellular",
        "month": "jun",
        "day_of_week": "mon",
        "duration": 285,
        "campaign": 2,
        "pdays": 999,
        "previous": 1,
        "poutcome": "failure",
        "emp.var.rate": 0,
        "cons.price.idx": 0,
        "cons.conf.idx": 0,
        "euribor3m": 0,
        "nr.employed": 0
      }

    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}

# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
