#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
and exports the information into a json file
"""

import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
response = requests.get(url)
employee_name = response.json()['name']

url2 = "https://jsonplaceholder.typicode.com/todos/" 
response2 = requests.get(url2)
todo_list = []
for titles in response2.json():
    if titles['userId'] == int(sys.argv[1]):
        if titles['completed'] == True:
            todo_list.append({"task": titles['title'],
                               "completed": titles['completed'],
                               "username": employee_name
                               })
json_data = {}
json_data[sys.argv[1]] = todo_list
with open("{}.json".format(sys.argv[1]), 'w') as file_json:
    json.dump(json_data, file_json)
