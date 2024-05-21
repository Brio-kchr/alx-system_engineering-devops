#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
and saves the data to a csv file
"""

import csv
import requests
import sys

url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
response = requests.get(url)
employee_name = response.json()['username']

url2 = "https://jsonplaceholder.typicode.com/todos/" 
response2 = requests.get(url2)
csv_file = sys.argv[1] + '.csv'
with open(csv_file, 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file, quoting=csv.QUOTE_ALL)

    for titles in response2.json():
        if titles['userId'] == int(sys.argv[1]):
            csv_writer.writerow([sys.argv[1], employee_name,
                                 titles['completed'],
                                 titles['title']])
