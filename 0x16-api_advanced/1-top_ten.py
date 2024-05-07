#!/usr/bin/pythin3
"""
Answering to How many subs
"""
import requests


headers = {"User-Agent": "mr-ndi/1.0"}


def is_valid_subreddit(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return True
    else:
        return False


def top_ten(subreddit):
    """method definition"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
