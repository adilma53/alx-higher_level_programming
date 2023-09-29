#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = urllib.request.Request(argv[1])
    with urllib.request.urlopen(url) as resp:
        print(dict(resp.headers).get("X-Request-Id"))