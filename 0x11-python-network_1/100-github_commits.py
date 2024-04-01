#!/usr/bin/python3
""" module documey """
import sys
import requests


def main():
    """ def com """
    owner = sys.argv[1]
    repo = sys.argv[2]
    limit = 10
    url = f'https://api.github.com/repos\
/{repo}/{owner}/commits?per_page={limit}'

    response = requests.get(url).json()
    for commit in response:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')


if __name__ == "__main__":
    main()