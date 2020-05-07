#!/usr/bin/python3
""" doc """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ doc """
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'user-agent': 'customclient/1.0'}
    query = {'limit': 100, 'after': after}
    request = requests.get(url, headers=header, params=query)
    if request.status_code == 200:
        nexts = request.json().get('data').get("after")
        if nexts is not None:
            recurse(subreddit, hot_list, nexts)
        info = request.json().get("data").get("children")
        for i in info:
            hot_list.append(i.get("data").get("title"))
        return (hot_list)
