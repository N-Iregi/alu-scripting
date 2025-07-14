#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """queries the Reddit API and prints the titles of first 10 hot posts"""
    hot_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:top_ten:v1.0 (by /u/yourusername)'}
    params = {"limit": 10}

    try:
        res =  requests.get(hot_url, params=params, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            print(None)
            return
        
        data = res.json().get('data', {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)

    except Exception:
       print(None) 