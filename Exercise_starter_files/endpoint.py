import requests
import json
import os

scoring_uri = "http://f42ea212-0d16-42c9-8a0a-3301f2569ea9.eastus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "KfUHuIJfEjOi7Cr7VHAgGMe9RsyDTdet"

data = {
  "Inputs": {
    "data": [
      {
        "age": 0,
        "job": "technician",
        "marital": "married",
        "education": "unknown",
        "default": "no",
        "housing": "no",
        "loan": "no",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "thu",
        "duration": 371,
        "campaign": 1,
        "pdays": 999,
        "previous": 1,
        "poutcome": "failure",
        "emp.var.rate": 1.1,
        "cons.price.idx": 92.1,
        "cons.conf.idx": -46.2,
        "euribor3m": 1.299,
        "nr.employed": 5228.1
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
