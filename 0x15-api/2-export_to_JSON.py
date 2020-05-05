#!/usr/bin/python3
""" ... """

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        if int(argv[1]):
            info = {"userId": argv[1]}
            url = "https://jsonplaceholder.typicode.com/todos"
            answer = requests.get(url, params=info).json()
            ids = argv[1]
            url = "https://jsonplaceholder.typicode.com/users/{}".format(ids)
            name = requests.get(url).json().get("username")
            columns = ['task', 'completed', 'username']
            to_dict = {}
            dicts = []
            for task in answer:
                task_ok = task.get("completed")
                value = [task.get("title"), task_ok, name]
                dicts.append(dict(zip(columns, value)))
            to_dict.update({"{}".format(ids): dicts})
            with open("{}.json".format(ids), 'w') as f:
                json.dump(to_dict, f)
