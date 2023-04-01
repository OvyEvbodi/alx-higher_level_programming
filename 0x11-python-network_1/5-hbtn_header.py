#!/usr/bin/python3

"""Takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""

import requests as req
import requests.exceptions as error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = req.get(url)
    try:
        print(res.headers["X-Request-Id"])
    except error.RequestException as err:
        pass
