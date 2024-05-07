#!/usr/bin/pythin3
"""
Answering to How many subs
"""
import requests


def number_of_subscribers(subreddit):
    """ A function to deliver the nbr of subs to the console"""
    header = {"User-Agent": "mr-ndi/1.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,allow_redirects=False, headers=headers)
    if reponse.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return (0)
