#!/usr/bin/python3

"""This script fetches https://alx-intranet.hbtn.io/status"""

import requests as req

url = "https://alx-intranet.hbtn.io/status"
res = req.get(url)

print(f"Body response:\n\t- type: {type(res.text)}\n\t- content: {res.text}")
