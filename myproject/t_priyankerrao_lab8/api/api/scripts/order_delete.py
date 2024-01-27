import requests

order_id = 4
api_url = f'http://localhost:8000/api/orders/{order_id}/'

response = requests.delete(api_url)

# Check the response status code
if response.status_code == 204:  # 204 No Content is often returned for successful DELETE requests
    print("Order deleted successfully.")
else:
    print("Error deleting the order.")
