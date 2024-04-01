#!/usr/bin/python3
""" module document """
import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    try:
         with urllib.request.urlopen(url) as req:
            body = req.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")