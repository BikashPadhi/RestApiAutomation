import requests
session = requests.session
payload = {'uname': 'name', 'password': 'pswd123'}
r = session.post('http://localhost/python', data=payload)
r = session.get('http://localhost/authenticated/resource')