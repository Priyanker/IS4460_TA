import requests
import json

# Define the API endpoint
api_url = 'http://localhost:8000/api/orders/'

# POST request to create an Order
order_data = {
    "customer": 3,
    "status": "pending"
}

response = requests.post(
    api_url, 
    data=json.dumps(order_data), 
    headers={'Content-Type': 'application/json'}
)

if response.status_code == 201:
    print("Order created successfully.")
else:
    print(f"Error creating order: {response.content}")