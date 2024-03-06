#!/usr/bin/python3
"first 10 hot posts"

import requests

def top_ten_posts(subreddit_name):
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit_name)
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(subreddit_url, headers=user_agent, allow_redirects=False)
    if response.status_code == 200:
        subreddit_data = response.json()
        for index in range(10):
            print(subreddit_data['data']['children'][index]['data']['title'])
    else:
        print(None)
