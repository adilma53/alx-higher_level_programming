#!/usr/bin/python3
"""
Python script that takes in a
URL and an email address, sends a POST request to
the passed URL with the email as a parameter
and display the res body
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    mail = {"email": argv[2]}
    req = requests.post(url, data=mail)
    print(req.text)
