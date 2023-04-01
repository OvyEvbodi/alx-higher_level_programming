#!/usr/bin/python3

"""Takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response
"""

import urllib.request as req
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    request = req.Request(url)
    with req.urlopen(request) as res:
        id = res.getheader("X-Request-Id")
        print(id)
