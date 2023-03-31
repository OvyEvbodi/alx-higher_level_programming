#!/usr/bin/python3

"""Takes in a URL, sends a request to the URL
and displays the body of the response
"""

import requests as req
from sys import argv


if __name__ == "__main__":
    url = arggv[1]
    res = req.get(url)
    code = res.status_code

    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(res.text)
