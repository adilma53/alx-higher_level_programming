#!/usr/bin/python3
"""script that takes in a URL,
sends a request and get 
response (decoded in utf-8)."""

from urllib import request, error
from sys import argv

try:
    with request.urlopen(argv[1]) as response:
        print(response.read().decode("utf-8"))
except error.HTTPError as e:
    print("Error code: {}".format(e.code))
