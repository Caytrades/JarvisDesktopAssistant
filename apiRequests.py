import requests

# Replace with your actual ngrok URL
ngrok_url = "https://ded1-103-211-54-32.ngrok-free.app"

# Define the endpoint and query parameter
endpoint = "/jarvis-query/"
query_param = {"query": "what is ur name?"}

# Send a GET request to the endpoint
response = requests.get(ngrok_url + endpoint, params=query_param)

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())