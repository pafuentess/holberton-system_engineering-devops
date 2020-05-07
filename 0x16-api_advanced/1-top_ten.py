#!/usr/bin/python3
""" doc """
import requests


def top_ten(subreddit):
    """ doc """
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    header = {'user-agent': 'customclient/1.0'}
    request = requests.get(url, headers=header)
    if request.status_code == 200:
        info = request.json()
        if "data" in info:
            for post in info.get("data").get("children"):
                print(post.get("data").get("title"))
        else:
            print(None)
    else:
        print(None)
        return
