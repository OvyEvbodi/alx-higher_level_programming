#!/usr/bin/python3

"""Takes 2 arguments in order to solve the given challenge
"""

import requests as req
from sys import argv

if __name__ == '__main__':
    repo_name = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    headers = {"Accept": "application/vnd.github+json"}

    res = req.get(url, headers=headers)
    commits = res.json()

    for commit in commits[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
