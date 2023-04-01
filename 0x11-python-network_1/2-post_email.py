#!/usr/bin/python3

"""akes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request as req
import urllib.parse as parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    info = {'email': argv[2]}
    data = parse.urlencode(info).encode('ascii')

    request = req.Request(url, data)
    with req.urlopen(request) as res:
        body = res.read()
        print(body.decode('utf-8'))
