#!/usr/bin/pythin3
"""
Answering to How many subs
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)
    if response.status_code == 404:
        return 0
    else:
        data = response.json()
        return data['data']['subscribers']
