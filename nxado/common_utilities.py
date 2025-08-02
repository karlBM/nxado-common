from google.auth import default
from google.auth.transport.requests import Request
import requests
import json



def get_google_credentials():
    # Load application default credentials
    credentials, project_id = google.auth.default()

    # Ensure credentials are valid and obtain an access token
    auth_request = Request()
    credentials.refresh(auth_request)

    # Get the access token
    access_token = credentials.token
    return access_token


def data_request(request):
    # Get credentials and generate an access token
    credentials, _ = default()
    auth_request = Request()
    credentials.refresh(auth_request)
    access_token = credentials.token

    # Set up the request to the BigQuery API (or your intended API)
    api_url = "https://nxado-common-559258860773.europe-west1.run.app/nxado-common"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Extract parameters from the request
    request_json = request.get_json()
    operation = request_json.get("operation")
    table = request_json.get("table")
    dataset = request_json.get("dataset")
    limit = request_json.get("limit", 10)  # Default limit

    # Construct payload
    payload = {
        "operation": operation,
        "dataset": dataset,
        "table": table,
        "limit": limit
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, json=payload)

    # Return the API response
    return response.text, response.status_code