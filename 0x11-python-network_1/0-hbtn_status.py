#!/usr/bin/python3
# A script that fetches url
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as req:
    html_content = req.read()
    print("Body response:")
    print("\t- type:", type(html_content))
    print("\t- content:", html_content)
    print("\t- utf8 content:", html_content.decode('utf-8'))
