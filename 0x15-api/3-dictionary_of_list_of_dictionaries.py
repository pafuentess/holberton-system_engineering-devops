#!/usr/bin/python3
""" ... """


import requests
from sys import argv
import csv
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    answer = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    ids = {}
    for user in users:
        ids.update({user.get("id"): user.get("username")})
    columns = ['task', 'completed', 'username']
    to_dict = {}
    for task in answer:
        user_id = task.get("UserId")
        dicts = to_dict.get(user_id)
        if dicts is None:
            dicts = []
        name = ids.get(user_id)
        completed = task.get("completed")
        values = [task.get("title"), completed, name]
        dicts.append(dict(zip(columns, values)))
        to_dict.update({user_id: dicts})
    with open("todo_all_employees.json", 'w') as f:
        json.dump(to_dict, f)
