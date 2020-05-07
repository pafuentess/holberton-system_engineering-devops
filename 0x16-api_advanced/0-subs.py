#!/usr/bin/python3
""" doc """
import requests


def number_of_subscribers(subreddit):
    """ doc """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    header = {'user-agent': 'customclient/1.0'}
    request = requests.get(url, headers=header)
    if request.status_code == 200:
        info = request.json()
        if "data" in info:
            data = info.get('data')
            return (data.get("subscribers"))
        else:
            return (0)
    else:
        return (0)
