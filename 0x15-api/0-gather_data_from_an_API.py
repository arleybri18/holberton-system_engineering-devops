#!/usr/bin/python3
""" This script consume API retrieve todos by user id """
import requests
from sys import argv


if __name__ == '__main__':
    """ get user id by argv use HTTP GET method """
    userId = argv[1]
    params = {'userId': userId}
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    res_todo = requests.get(url_todo, params=params)
    todos = res_todo.json()
    comp = 0
    todo_list = []
    for todo in todos:
        if todo['completed']:
            todo_list.append(todo['title'])
            comp += 1
    params = {'id': userId}
    url_user = 'https://jsonplaceholder.typicode.com/users'
    res_user = requests.get(url_user, params=params)
    user = res_user.json()[0]
    name = user['name']
    print("Employee {} is done with tasks({}/{}):".
          format(name, comp, len(todos)))
    for todo in todo_list:
        print('\t {}'.format(todo))
