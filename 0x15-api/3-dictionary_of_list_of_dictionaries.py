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
    url_user = 'https://jsonplaceholder.typicode.com/users'
    res_user = requests.get(url_user)
    users = res_user.json()
    result = {}
    for user in users:
        username = user['username']
        userId = user['id']
        list_tasks = []
        params = {'userId': userId}
        url_todo = 'https://jsonplaceholder.typicode.com/todos'
        res_todo = requests.get(url_todo, params=params)
        todos = res_todo.json()
        for todo in todos:
            dict_task = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': username}
            list_tasks.append(OrderedDict(dict_task))
            result[userId] = list_tasks
        with open('todo_all_employees.json', 'w') as f:
            f.write(json.dumps(result))
