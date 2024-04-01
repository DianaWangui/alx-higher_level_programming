#!/usr/bin/python3
""" module doc """
import requests
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    # if r.status_code == 200:
    x_request_id = r.headers.get('X-Request-Id')
    print(x_request_id)
