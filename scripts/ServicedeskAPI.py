import sys, requests


def test():
    print("Hello - test.")

def new_incident():
    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_agent():
    url = 'https://apt-servicedesk.azurewebsites.net/api/agent/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_agent(passthrough):
    url = 'https://apt-servicedesk.azurewebsites.net/api/agent/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_incident():
    url = 'https://apt-servicedesk.azurewebsites.net/api/incident/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_department():
    url = 'https://apt-servicedesk.azurewebsites.net/api/department/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_department():
    url = 'https://apt-servicedesk.azurewebsites.net/api/department/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)


def get_category():
    url = 'https://apt-servicedesk.azurewebsites.net/api/category/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_category():
    url = 'https://apt-servicedesk.azurewebsites.net/api/category/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
