import requests
url = 'http://127.0.0.1:5000/api/tickets'

r = requests.post(url)

# Response, status etc
print(r.text)
print(r.status_code)