import requests

headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'username':'niceusername','password':'123456'}

session = requests.Session()

session.post('https://admin.example.com/login.php',headers=headers,data=payload)

# the session instance holds the cookie. So use it to get/post later.
# e.g. session.get('https://example.com/profile')