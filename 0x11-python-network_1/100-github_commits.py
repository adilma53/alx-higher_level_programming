#!/usr/bin/python3
"""
GitHub API: Fetch the latest 10 commits from a repository
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[1], argv[2]
    )
    req = requests.get(url)
    body = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                body[i].get("sha"),
                body[i].get("commit").get("author").get("name")
            ))
    except IndexError:
        pass
