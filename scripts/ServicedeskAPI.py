import sys, requests, json, random, string

def test():
    print("Hello - test.")

def new_incident():
    url = 'http://127.0.0.1:5000/api/incident/'
    rand1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    data = {'incident': {'subject': '{}'.format(rand1),
                         'description': '{}@test.com'.format(rand1),
                         'priority': '',
                         'status': '2',
                         'agent_group': '',
                         'agent_assigned': '',
                         'department': '',
                         'category': '',
                         'sub_category': '',
                         'requester': '1'}
        }
    print(data)
    r = requests.post(url, json=data)
    print(r.text)
    print(r.status_code)

def new_agent():
    url = 'http://127.0.0.1:5000/api/agent/'

    rand1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    data = {'agent': {'name': 'test{}'.format(rand1),
                      'email_address': 'test{}@test.com'.format(rand1)},
        }
    print(data)
    r = requests.post(url, json=data)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_agent():
    url = 'http://127.0.0.1:5000/api/agent/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def delete_agent():
    url = 'http://127.0.0.1:5000/api/agent/3'

    r = requests.delete(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_incident():
    url = 'http://127.0.0.1:5000/api/incident/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_department():
    url = 'http://127.0.0.1:5000/api/department/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_department():
    url = 'http://127.0.0.1:5000/api/department/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)


def get_category():
    url = 'http://127.0.0.1:5000/api/category/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_category():
    url = 'http://127.0.0.1:5000/api/category/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)


def get_status():
    url = 'http://127.0.0.1:5000/api/status/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_status():
    url = 'http://127.0.0.1:5000/api/status/'
    data = {'status': {'name': 'Open'}}
    r = requests.post(url, json=data)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_priority():
    url = 'http://127.0.0.1:5000/api/priority/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_priority():
    url = 'http://127.0.0.1:5000/api/priority/'

    data = {'priority': {'name': 'Urgent'},
        }
    print(data)
    r = requests.post(url, json=data)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_impact():
    url = 'http://127.0.0.1:5000/api/impact/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_impact():
    url = 'http://127.0.0.1:5000/api/impact/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_sub_category():
    url = 'http://127.0.0.1:5000/api/sub_category/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_sub_category():
    url = 'http://127.0.0.1:5000/api/sub_category/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_urgency():
    url = 'http://127.0.0.1:5000/api/urgency/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_urgency():
    url = 'http://127.0.0.1:5000/api/urgency/'

    r = requests.post(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def get_agent_group():
    url = 'http://127.0.0.1:5000/api/agent_group/'

    r = requests.get(url)

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_agent_group():
    url = 'http://127.0.0.1:5000/api/agent_group/'
    r = requests.post(url, data = json.dumps(data))

    # Response, status etc
    print(r.text)
    print(r.status_code)

def new_sub_category():
    url = 'http://127.0.0.1:5000/api/user/'
    rand1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    data = {'user': {'email_address': '{}'.format(rand1),
                         'name': '{}@test.com'.format(rand1),
                         'user_type': 'requester'}
    }
    rand1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
    data2 = {'user': {'email_address': '{}@test.com'.format(rand1),
                         'name': '{}'.format(rand1),
                         'user_type': 'agent'}
    }
    print(data)
    r = requests.post(url, json=data)
    print(r.text)
    print(r.status_code)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
