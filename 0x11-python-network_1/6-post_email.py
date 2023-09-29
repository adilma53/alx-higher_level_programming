#!/usr/bin/python3
"""
Python script that takes in a
URL and an email address, sends a POST request to
the passed URL with the email as a parameter
and display the res body
"""
import requests
from sys import argv


url = argv[1]
mail = {"email": argv[2]}
data = requests.post(url, data=mail)
print(data.text)
