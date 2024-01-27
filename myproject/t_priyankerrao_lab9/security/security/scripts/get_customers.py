import requests

# Define the API endpoint
api_url = 'http://localhost:8000/api/customers/'

# create a token variable.
token = 'b06042ba0a8943966705a7aa2feadde982775685'

# Pass the token in the header.
headers = {
    'Authorization': f'Token {token}'
}

# Get customers using a single Get request
response = requests.get(api_url, headers=headers)

print(response.status_code)

# Check the response status and content
if response.status_code == 200:
    print(f"Customers retrieval successful. {response.text}")
else:
    print(f"Customers retrieval failed. {response.text}")
