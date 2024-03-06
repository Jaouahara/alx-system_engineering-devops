#!/usr/bin/python3
"subscribers count"

import requests

def number_of_subscribers(subreddit_name):
    subreddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit_name)
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(subreddit_url, headers=user_agent, allow_redirects=False)
    subreddit_data = response.json()
    if response.status_code != 200:
        return 0
    else:
        return subreddit_data['data']['subscribers']
