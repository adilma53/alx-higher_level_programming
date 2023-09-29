#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request and get reponse header
"""

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get("X-Request-Id"))