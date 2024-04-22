#!/usr/bin/python3
"""Exports data to JSON format"""

from json import dump
from requests import get
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    respond = get(url)
    u_name = respond.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    respond = get(url)
    tasks = respond.json()
    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": u_name
                                    })
    with open('{}.json'.format(user_id), 'w') as file:
        dump(dictionary, file)
