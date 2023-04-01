#!/usr/bin/python3

"""Takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    msg = ""

    if len(argv) >= 1:
        msg = argv[1]
    res = req.post(url, data={"q": msg})

    try:
        data = res.json()
        if not data:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
