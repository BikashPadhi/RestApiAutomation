import responses
import requests

# API TESTING

responses.add(responses.GET,'http://www.dropbox.com/asif'
                ,body='{"error":"not found"}',status=404)

NewResponse =requests.get('http://www.dropbox.com/asif' )

NewResponse2=requests.get('http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=demo')

print NewResponse.text
print NewResponse.status_code


print NewResponse2.text
print NewResponse2.status_code
print NewResponse2.json()