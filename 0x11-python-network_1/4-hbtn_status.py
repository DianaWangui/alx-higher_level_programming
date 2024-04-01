#!/usr/bin/python3
""" module document """
import requests
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print(f'Body response:\n\t- type {type(r.text)}\n\t- content: {r.text}')
