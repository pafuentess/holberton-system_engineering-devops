#!/usr/bin/python3
""" ... """


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
            name = requests.get(url).json().get("name")
            task_ok = []
            for task in answer:
                if task.get("completed") is True:
                    task_ok.append(task.get("title"))
            lentask_ok = len(task_ok)
            lenanswer = len(answer)
            if name:
                print("Employee {} is done with tasks({}/{}):".
                      format(name, lentask_ok, lenanswer))
                for name_task in task_ok:
                    print("\t {}".format(name_task))
