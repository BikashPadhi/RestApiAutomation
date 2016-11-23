import requests

r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})

print(r.status_code, r.reason)

print "Status CODE And Reason Printed"

print(r.text[:300] + '...')