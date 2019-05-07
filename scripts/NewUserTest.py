import requests

url = 'http://127.0.0.1:5000/api/user/'

data = {'user': {'email_address': 'ashley.collinge@outlook.com',
                        'name': 'Ashley Collinge',
                        'user_type': 'agent'}
}

r = requests.post(url, json=data)

# Response, status etc
print(r.text)
print(r.status_code)