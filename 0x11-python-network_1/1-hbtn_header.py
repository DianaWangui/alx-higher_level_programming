#!/usr/bin/python3
""" module doc """
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as req:
    headers = req.headers
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
