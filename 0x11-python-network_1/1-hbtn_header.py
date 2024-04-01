#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as req:
    headers = req.headers
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
