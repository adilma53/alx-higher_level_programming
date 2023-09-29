#!/usr/bin/python3
"""
script that
fetches https://alx-intranet.hbtn.io/status
"""

import requests

request = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(request.text)))
print("\t- content: {}".format(request.text))
