import requests
import json

# Define the API endpoint
api_url = 'http://localhost:8000/api/customers/'

# Customer data as a JSON object
customer_data = {
    "name": "Customer X",
    "email": "customerX@example.com",
    "phone_number": "8014445555"
}

# Create customers using a single POST request
response = requests.post(api_url, data=json.dumps(customer_data), headers={'Content-Type': 'application/json'})

# Check the response status and content
if response.status_code == 201:
    print("Customers created successfully.")
else:
    print("Error creating customers.")
