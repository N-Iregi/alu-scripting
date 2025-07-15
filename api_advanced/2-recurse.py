#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. 
If no results are found for the given subreddit, the function should
return None.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively collects titles of all hot articles in a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:recurse:v1.0 (by /u/yourusername)'}
    
    # query string components
    params = {"limit": 100}
    if after: # if this is not 1st page(after is not none)
        params["after"] = after

    # make a request to url
    try:
        res = requests.get(url, headers=headers, params=params, allow_redirects = False)

        # check for status code
        if res.status_code != 200:
            return None
        
        # retrieve data key of res which is listing
        data = res.json().get('data', {})

        # retrieve children key in data
        children = data.get('children', [])

        # get data part of children which has titles of hot articles
        for post in children:
            post_data = post.get("data", {})
            hot_title = post_data.get("title")

            #append titles to the list
            hot_list.append(hot_title)

        # check if after was sent and get its value for recursive call use
        after = data.get("after")

        if after:
            return recurse(subreddit, hot_list, after)
        
        # if no more pages are available
        return hot_list
    
    except Exception:
        return None