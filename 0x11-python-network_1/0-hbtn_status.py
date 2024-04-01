#!/usr/bin/python3
# A script that fetches url
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as req:
    html_content = req.read()
    utf_data = html_content.decode('utf-8')
    data_type = type(html_content)
    print(f'Body response:\n\t- type: {data_type}\n\t- \
    content{html_content}\n\t- utf8 content: {utf_data}')
