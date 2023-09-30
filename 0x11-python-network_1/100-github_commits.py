#!/usr/bin/python3
"""
GitHub API: Fetch the latest 10 commits from a repository
"""
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    base_url = f'https://api.github.com/repos/\
        {owner_name}/{repository_name}/commits'

    response = requests.get(base_url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(f'Error: Unable to fetch commits. Status code:\
                {response.status_code}')
