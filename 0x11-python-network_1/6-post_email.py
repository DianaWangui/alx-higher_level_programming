#!/usr/bin/python3
""" module doc """
import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data=data)
    print(r.text)