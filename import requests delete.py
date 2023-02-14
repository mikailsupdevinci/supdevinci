import requests

response = requests.delete('http://localhost:5000/employees/4')
print(response.json())
