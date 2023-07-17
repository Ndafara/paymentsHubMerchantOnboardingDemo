import requests
import json
import pprint

# Set the request parameters
url = 'https://enrollment-api-sandbox.paymentshub.com'
path = '/enroll/application'

bearer_token = 'PUT_YOUR_ACCESS_TOKEN_HERE'

# Set proper headers
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + bearer_token}

# Set the mandatory urlencoded body
payload = {
    "agent": 'PUT_YOUR_AGENT_ID_HERE',
    "applicationName": "Test Application 1",
    "externalKey": "012345-ABC",
    "plan": {
        "planId": 'PUT_YOUR_PLAN_ID_HERE'
    },
    "principals": [
        {
            "firstName": "Jane",
            "lastName": "Jackson",
            "socialSecurityNumber": "456321798",
            "dateOfBirth": "1955-12-25",
            "phoneNumber": "1234567890",
            "email": "user@example.com",
            "street": "123 Selah Way",
            "street2": "Suite 123",
            "zipCode": "12345",
            "city": "South Burlington",
            "state": "VT",
            "equityOwnershipPercentage": 50,
            "title": "ceo",
            "isPersonalGuarantor": True,
            "driverLicenseNumber": "ABC1234567890",
            "driverLicenseIssuedState": "MI"
        },
        {
            "firstName": "Jeremy",
            "lastName": "Coelman",
            "socialSecurityNumber": "897213546",
            "dateOfBirth": "1977-12-25",
            "phoneNumber": "1234567890",
            "email": "user@example.com",
            "street": "1234 Finwood Drive",
            "zipCode": "12345",
            "city": "Red Bank",
            "state": "NJ",
            "equityOwnershipPercentage": 50,
            "title": "manager",
            "isPersonalGuarantor": False,
            "driverLicenseNumber": None,
            "driverLicenseIssuedState": None
        }
    ],
    "business": {
        "corporateName": "Joe's Spaceage Stereo",
        "dbaName": "Jo Jackson Spaceage Stereo",
        "businessType": "C",
        "federalTaxIdNumber": "123567890",
        "federalTaxIdType": "EIN",
        "mcc": "0742",
        "phone": "1234567890",
        "email": "user@example.com",
        "websites": [
            {
                "url": "https://example.com",
                "websiteCustomerServiceEmail": "customer-service-email@example.com",
                "websiteCustomerServicePhoneNumber": "1234567890"
            }
        ],
        "averageTicketAmount": 5000,
        "averageMonthlyVolume": 1250000,
        "highTicketAmount": 125000,
        "merchandiseServicesSold": "Audio components and services",
        "percentOfBusinessTransactions": {
            "cardSwiped": 65,
            "keyedCardPresentNotImprinted": 20,
            "mailOrPhoneOrder": 0,
            "internet": 15
        },
        "businessContact": {
            "firstName": "Roy",
            "lastName": "Martin",
            "socialSecurityNumber": "123446789",
            "dateOfBirth": "1947-11-05",
            "street": "123 Late Avenue",
            "street2": "",
            "zipCode": "12345",
            "city": "South Burington",
            "state": "VT",
            "phoneNumber": "1234567890",
            "email": "user@example.com"
        },
        "statementDeliveryMethod": "electronic",
        "businessAddress": {
            "dba": {
                "street": "1234 Clinton St",
                "city": "South Burlington",
                "state": "VT",
                "zipCode": "12345"
            },
            "corporate": {
                "street": "1234 Sun Valley Rd",
                "city": "South Burlington",
                "state": "VT",
                "zipCode": "12345"
            },
            "shipTo": {
                "street": "1234 Saint James Drive",
                "city": "South Burlington",
                "state": "VT",
                "zipCode": "12345"
            }
        }
    },
    "bankAccount": {
        "abaRouting": "072403473",
        "accountType": "checking",
        "demandDepositAccount": "01382634850"
    }
}

# Convert the payload to JSON String
json_payload = json.dumps(payload)

# Do the HTTP request
response = requests.post(url + path, headers=headers, data=json_payload)

# Check for HTTP codes other than 200
if response.status_code != 200:
    pprint.pprint(f'Status: {response.status_code} Headers: {response.headers} Error Response: {response.json()}')
    exit()

# Get the JSON response
data = response.json()
pprint.pprint(data, indent=2)
