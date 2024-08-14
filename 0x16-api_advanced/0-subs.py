#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import json
import requests



def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    #u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': 'myRedditAp/0.0.1'
        #'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']

# #!/usr/bin/python3
# """
# this script uses Reddit API to give the number of subscribers """

# import json
# import requests


# def number_of_subscribers(subreddit):
#     headers = {
#         'User-Agent': 'myRedditAp/0.0.1'
#     }

#     url = f'https://www.reddit.com/r/{subreddit}/about.json'

#     response = requests.get(url, headers=headers, allow_redirects=False)

#     if response.status_code == 200:
#         data = response.json()

#         return data.get('data', {}).get('subscribers')
#     else:
#         return 0
