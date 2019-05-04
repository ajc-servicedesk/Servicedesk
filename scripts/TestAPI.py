import requests
url = 'https://apt-servicedesk.azurewebsites.net/api/incident/'

r = requests.post(url)

# Response, status etc
print(r.text)
print(r.status_code)