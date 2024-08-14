#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import requests
import sys


def top_ten(subreddit):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
# #!/usr/bin/python3
# """
# Gives limit of top ten titles of any subreddit
# """


# import json
# import requests


# def top_ten(subreddit):
#     url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
#     headers = {'User-Agent': 'myRedditApp/0.0.1'}

#     try:
#         response = requests.get(url, headers=headers, allow_redirects=False)
#         if response.status_code == 200:
#             posts = response.json().get('data', {}).get('children', [])
#             if posts:
#                 for post in posts:
#                     print(post['data']['title'])
#             else:
#                 print(None)
#         else:
#             print(None)
#     except requests.RequestException:
#         print(None)
