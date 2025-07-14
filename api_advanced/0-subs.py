#!/usr/bin/python3
"""Fetches number of subscribers for a given subreddit."""

import requests

def number_of_subscribers(subreddit):
    """Returns total subscribers for a subreddit. Returns 0 if invalid."""
    subred_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Python:subreddit.subscriber.counter:v1.0 (by /u/cert_iva)'
    }

    try:
        res = requests.get(subred_url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return 0
        return res.json()["data"]["subscribers"]
    except Exception:
        return 0
