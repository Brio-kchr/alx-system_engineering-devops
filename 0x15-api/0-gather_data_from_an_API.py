#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys

url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
response = requests.get(url)
employee_name = response.json()['name']

url2 = "https://jsonplaceholder.typicode.com/todos/" 
response2 = requests.get(url2)
total_tasks = 0
done_tasks = 0
title_list = []
for titles in response2.json():
    if titles['userId'] == int(sys.argv[1]):
        total_tasks += 1
        if titles['completed'] == True:
            done_tasks += 1
            title_list.append(titles['title'])
print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
for title in title_list:
    print("\t {}".format(title))
