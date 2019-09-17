#!/usr/bin/python3
""" This script consume API retrieve todos by user id
    export data to json
"""
from collections import OrderedDict
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    """ get user id by argv use HTTP GET method """
    userId = argv[1]
    params = {'userId': userId}
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    res_todo = requests.get(url_todo, params=params)
    todos = res_todo.json()
    params = {'id': userId}
    url_user = 'https://jsonplaceholder.typicode.com/users'
    res_user = requests.get(url_user, params=params)
    user = res_user.json()[0]
    username = user['username']
    list_tasks = []
    for todo in todos:
        dict_task = {
            'task': todo['title'],
            'completed': todo['completed'],
            'username': username}
        list_tasks.append(OrderedDict(dict_task))
    result = {argv[1]: list_tasks}
    with open('{}.json'.format(argv[1]), 'w') as f:
        f.write(json.dumps(result))
