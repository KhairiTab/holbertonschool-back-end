#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her To Do list progress.
"""
import json
import requests


def TODO_PROGRESS():
    users_url = 'https://jsonplaceholder.typicode.com/users'
    all_users = requests.get(users_url).json()
    information = {}

    for user in all_users:
        user_id = user['id']
        name = user['username']
        todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id)
        todos = requests.get(todos).json()
        tasks = [{"username": name, "task": todo["title"],
                  "completed": todo["completed"]} for todo in todos]
        information[user_id] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(information, file)


if __name__ == "__main__":
    TODO_PROGRESS()
