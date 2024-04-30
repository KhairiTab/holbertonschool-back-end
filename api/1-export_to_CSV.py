#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her To Do list progress.
"""
import requests
import sys


def TODO_PROGRESS():
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user_url).json().get('username')
    todo_response = requests.get(todos_url).json()

    with open('{}.csv'.format(user_id), 'w+') as file:
        for todo in todo_response:
            information = '"{}","{}","{}","{}"\n'.format(
                user_id, name, todo.get('completed'), todo.get('title'))
            file.write(information)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        TODO_PROGRESS()
