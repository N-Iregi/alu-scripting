#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    """

    subred_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'script:0-subs.py:v1.0 by (/u/cert_iva)'}

    try:
        res = requests.get(subred_url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return 0
        return res.json()["data"]["subscribers"]
    except Exception:
        return 0