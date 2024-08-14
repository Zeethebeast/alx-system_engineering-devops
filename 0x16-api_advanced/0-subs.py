#!/usr/bin/python3
"""
this script uses Reddit API to give the number of subscribers """

import json
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'myRedditAp/0.0.1'
    }

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        return data.get('data', {}).get('subscribers')
    else:
        return 0