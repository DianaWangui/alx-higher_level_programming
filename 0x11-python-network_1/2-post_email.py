#!/usr/bin/python3
""" module doc """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    email_info = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=email_info) as req:
        body = req.read().decode('utf-8')
        print(body)
