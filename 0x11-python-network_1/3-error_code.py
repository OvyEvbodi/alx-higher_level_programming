#!/usr/bin/python3

"""Takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import urllib.request as req
import urllib.error as err
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    request = req.Request(url)

    try:
        with req.urlopen(request) as res:
            body = res.read().decode('utf-8')
            print(body)
    except err.HTTPError as err:
        print(f"Error code: {err.code}")
