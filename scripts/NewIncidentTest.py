import requests

url = 'http://127.0.0.1:5000/api/incident/'

data = {'incident': {'subject': '{}'.format("Emails aren't working"),
                        'description': 'the screen isn on',
                        'priority': '3', # 
                        'status': '3', # 
                        'agent_group': '',
                        'agent_assigned': '',
                        'department': '',
                        'category': '3', # 
                        'sub_category': '',
                        'requester': ''}
}

r = requests.post(url, json=data)

# Response, status etc
print(r.text)
print(r.status_code)