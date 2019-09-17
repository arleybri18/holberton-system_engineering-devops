#!/usr/bin/python3
""" This script consume API retrieve todos by user id
    export data to csv export data to csv
"""
import csv
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
    list_rows = []
    for todo in todos:
        row = list([argv[1], username, str(todo['completed']), todo['title']])
        list_rows.append(row)
    with open('2.csv', 'wt') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(list_rows)
