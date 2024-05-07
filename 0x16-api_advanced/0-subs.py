<<<<<<< HEAD
#!/usr/bin/pythin3
"""
Answering to How many subs
"""
=======
#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
>>>>>>> b1579132c18bc25c86de84ae69c2671723dd7554
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
