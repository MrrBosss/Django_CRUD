import requests

headers = {'Authorization': 'Bearer 355694be3ac97f0077f75835182b5d9a4ddb2567'}
endpoint = "http://localhost:8000/api/products/" 

data = {
    'title': 'This field is done'
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
