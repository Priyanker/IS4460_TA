import requests
import json

order_id = 4
api_url = f'http://localhost:8000/api/orders/{order_id}/'

updated_order_data = {
    "customer": 1,  
    "status": "completed"
}

# Send a PUT request to update the order
response = requests.put(api_url, data=json.dumps(updated_order_data), headers={'Content-Type': 'application/json'})

# Check the response status code and content
if response.status_code == 200:
    print("Order updated successfully.")
else:
    print("Error updating the order.")
