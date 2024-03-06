#!/usr/bin/python3
"""
Using reddit's API
"""
import requests

after_param = None

def recursive_top_ten(subreddit_name, hot_list=[]):
    """returning top ten post titles recursively"""
    global after_param
    user_agent = {'User-Agent': 'api_advanced-project'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit_name)
    parameters = {'after': after_param}
    results = requests.get(subreddit_url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after_param = after_data
            recursive_top_ten(subreddit_name, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_data in all_titles:
            hot_list.append(title_data.get("data").get("title"))
        return hot_list
    else:
        return None
