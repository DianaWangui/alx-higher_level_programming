#!/usr/bin/python3
""" module document """
import requests
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    data = r.text
    data_type = type(data)
    print(f'Body response:\n\t- type: {data_type}\n\t- content: {data}')
