#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her To Do list progress.
"""
import json
import requests
import sys


def TODO_PROGRESS():
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user_url).json().get('username')
    todo_response = requests.get(todos_url).json()
    tasks = []

    with open('{}.json'.format(user_id), 'w+') as file:
        for todo in todo_response:
            task = {"task": todo.get("title"),
                    "completed": todo.get("completed"), "username": name}
            tasks.append(task)
        information = {user_id: tasks}
        file.write(json.dumps(information))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        TODO_PROGRESS()
