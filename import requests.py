import requests

url = 'http://127.0.0.1:5000/employees'
data = {'id': 'New Product', 'name': 'This is a new product', 'position':'test','salary': 49.99}
response = requests.post(url, json=data)

if response.ok:
    print(response.json())
else:
    print(response.text)
