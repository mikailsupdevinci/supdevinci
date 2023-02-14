import requests

url = 'http://127.0.0.1:5000/employees/POST'  # URL de l'API
data = {'name': 'John', 'age': 30}   # données à envoyer

response = requests.post(url, json=data)  # envoyer la requête POST avec les données en JSON

if response.status_code == 200:
    print('Requête envoyée avec succès !')
else:
    print(f'Erreur {response.status_code} lors de l\'envoi de la requête')
