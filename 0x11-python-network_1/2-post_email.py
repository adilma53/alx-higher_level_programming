#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print("Your email is:", body)
