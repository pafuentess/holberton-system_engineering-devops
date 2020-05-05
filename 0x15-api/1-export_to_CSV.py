#!/usr/bin/python3
""" ... """

import csv
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
            with open("{}.csv".format(ids), 'w') as f:
                columns = ['id', 'name', 'status', 'title']
                fill = csv. DictWriter(f, fieldnames=columns,
                                       quoting=csv.QUOTE_ALL)
                for task in answer:
                    task_ok = task.get("completed")
                    fill.writerow({'id': '{}'.format(ids),
                                   'name': '{}'.format(name),
                                   'status': '{}'.format(str(task_ok)),
                                   'title': '{}'.format(task.get("title"))})
