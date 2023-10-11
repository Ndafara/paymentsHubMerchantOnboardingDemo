import requests
import pprint

# Set the external key
externalKey = 'externalKey'

# Set the request parameters
url = 'https://enrollment-api-sandbox.paymentshub.com'
path = '/enroll/application/submit/' + externalKey

# Set proper headers
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Authorization': 'Bearer PUT_YOUR_TOKEN_HERE'}

# Do the HTTP request
response = requests.put(url, headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
