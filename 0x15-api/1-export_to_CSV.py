#!/usr/bin/python3
"""
Module of a function to fetch a TODOlist of an employee and
 export it to a csv file "<employeeid>.csv"
"""
import csv
import requests


def export_todo(employee_id: int):
    """
    Fetches employee todo list and exports it
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(employee_id)
    )
    employee_alias = response.json().get("username")
    if employee_alias is None:
        return

    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )
    todo_list = response.json()
    with open("{}.csv".format(employee_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            taskwriter.writerow([employee_id, employee_alias,
                                 task.get('completed'),
                                 task.get('title')])


if __name__ == "__main__":
    from sys import argv

    export_todo(int(argv[1]))
