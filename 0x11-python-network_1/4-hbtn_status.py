#!/usr/bin/python3

"""This script fetches https://alx-intranet.hbtn.io/status"""

import requests as req


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = req.get(url)

    print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
