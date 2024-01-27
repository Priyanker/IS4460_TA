import requests

# Define the token endpoint URL
token_url = 'http://localhost:8000/api-token-auth/'

# Your authentication credentials (username and password)
credentials = {
    'username': 'exampleuser1',
    'password': 'asdert123',
}

# Send a POST request to obtain a token
response = requests.post(token_url, data=credentials)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response to access the token
    token_data = response.json()
    print('token_data', token_data)

    # Extract the token from the response
    token = token_data.get('token')
    if token:
        print(f"Authentication successful. Token: {token}")
    else:
        print("Token not found in response.")
else:
    print(f"Authentication failed. Status code: {response.status_code}")
    with open('logfile.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
