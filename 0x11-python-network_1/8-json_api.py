#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}

    response = requests.post(url, data=data)

    try:
        user_info = response.json()

        if user_info:
            print("[{}] {}".format(user_info.get('id'), user_info.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
