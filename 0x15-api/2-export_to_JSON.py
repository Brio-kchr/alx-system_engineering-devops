#!/usr/bin/python3
"""
Module of a function to fetch a TODOlist of an employee and
 export it to a csv file "<employeeid>.json"
"""
import json
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

    todo_list = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_alias
        }
        for task in todo_list
    ]
    json_data = {}
    json_data[employee_id] = todo_list
    with open("{}.json".format(employee_id), 'w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    from sys import argv

    export_todo(int(argv[1]))
