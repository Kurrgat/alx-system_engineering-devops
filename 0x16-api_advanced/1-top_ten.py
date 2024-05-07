#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot
posts for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    subreddit = sys.argv[1] if len(sys.argv) > 1 else None
    if subreddit:
        top_ten(subreddit)
    else:
        print("Please pass an argument for the subreddit to search.")
