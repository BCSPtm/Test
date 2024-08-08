#!/usr/bin/env python3
import requests
import base64
import json

data = {
    "url": "https://books.toscrape.com/",
    "httpResponseBody": True
}

headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': '150b4b80-e035-46e0-8b4c-6278a512f53a'
}

response = requests.post('https://api.proxyscrape.com/v3/accounts/freebies/scraperapi/request', headers=headers, json=data)

if response.status_code == 200:
    json_response = response.json()
    if 'browserHtml' in json_response['data']:
        print(json_response['data']['browserHtml'])
    else:
        print(base64.b64decode(json_response['data']['httpResponseBody']).decode())
else:
    print("Error:", response.status_code)
