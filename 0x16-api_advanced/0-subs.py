#!/usr/bin/python3
"""
function that queries the Reddit API
Returns the number of total subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of total subscribers of a subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {"User-Agent": "MyUser"}
    response = requests.get(url, allow_redirects=False, headers=header)

    if response.status_code == 404:
        return (0)
    else if response.status_code == 200:
        req = int(response.json().get("data").get("subscribers"))
        return (req)
