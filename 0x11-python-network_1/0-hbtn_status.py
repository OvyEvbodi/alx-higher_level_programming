#!/usr/bin/python3

"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as req


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = req.Request(url)
    with req.urlopen(request) as res:
        body = res.read()
        print(f"Body response:\n\t- type: {type(body)}\n\t- content: \
                {body}\n\t- utf8 content: {body.decode('utf-8')}")
