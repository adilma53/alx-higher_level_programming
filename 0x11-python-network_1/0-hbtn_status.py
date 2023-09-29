#!/usr/bin/python3
"""fetch a URL and displays the value of the variable"""


from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

req = request.Request(url)
with request.urlopen(req) as response:
    content = response.read()

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", content.decode('utf-8'))
