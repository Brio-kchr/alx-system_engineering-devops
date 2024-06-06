#!/usr/bin/python3
"""Module for task 0"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    response  = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return int(response.json().get("data").get("subscribers"))
