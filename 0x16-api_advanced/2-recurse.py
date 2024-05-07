#!/usr/bin/python3
"""
Queries the Reddit API recursively
"""

import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)  # Corrected indentation

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    subreddit = sys.argv[1] if len(sys.argv) > 1 else None
    if subreddit:
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
    else:
        print("Please pass an argument for the subreddit to search.")
