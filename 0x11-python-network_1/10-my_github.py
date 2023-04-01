#!/usr/bin/python3

"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests as req
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = f'https://api.github.com/users/{username}'
    headers = {"Authorization": f"Bearer {password}",
               "Accept": "application/vnd.github+json"}

    res = req.get(url, headers=headers)
    print(res.json().get("id"))
