#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    mail = {"email": argv[2]}
    data = urllib.parse.urlencode(mail)
    data = data.encode("ascii")

    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as reques:
        print(reques.read().decode("utf-8"))
