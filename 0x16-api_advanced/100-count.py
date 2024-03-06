#!/usr/bin/python3
"""
Module for count_words function
"""
import requests

def count_words_in_subreddit(subreddit_name, keywords_list, new_after='',
                             word_count={}):
    """
    A recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords
    """

    keywords_list = map(lambda x: x.lower(), keywords_list)
    keywords_list = list(keywords_list)

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit_name),
                       headers={'User-Agent': 'Custom'},
                       params={'after': new_after},
                       allow_redirects=False)

    if res.status_code != 200:
        return

    try:
        response = res.json().get('data', None)

        if response is None:
            return
    except ValueError:
        return

    children = response.get('children', [])

    for post in children:
        title = post.get('data', {}).get('title', '')
        for keyword in keywords_list:
            for word in title.lower().split():
                if keyword == word:
                    word_count[keyword] = word_count.get(keyword, 0) + 1

    new_after = response.get('after', None)

    if new_after is None:
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda x: x[1],
                                   reverse=True)

        for item in sorted_word_count:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
        return

    return count_words_in_subreddit(subreddit_name, keywords_list,
                                    new_after, word_count)
