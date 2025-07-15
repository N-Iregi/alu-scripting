#!/usr/bin/python3
"""
Recursively queries Reddit's hot posts and counts keyword occurrences
in titles. Results are printed sorted by count and alphabetically.
"""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """Counts occurrences of keywords from word_list in hot post titles."""
    # Initialize the word_count dictionary once
    if word_count is None:
        word_count = {}
        for word in word_list:
            word_lower = word.lower()
            if word_lower in word_count:
                word_count[word_lower] += 0  # duplicate word, ignore repeat
            else:
                word_count[word_lower] = 0

    # Setup request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:count_words:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        res = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if res.status_code != 200:
            return  # Invalid subreddit or error, print nothing

        data = res.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            words = title.split()

            for word in words:
                clean_word = word.strip(".,!?\"':;()[]{}").lower()
                if clean_word in word_count:
                    word_count[clean_word] += 1

        # Recurse if more pages exist
        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, word_count, after)

        # Base case: print results
        sorted_counts = sorted(
            [(w, c) for w, c in word_count.items() if c > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_counts:
            print(f"{word}: {count}")

    except Exception:
        return  # On any failure, print nothing