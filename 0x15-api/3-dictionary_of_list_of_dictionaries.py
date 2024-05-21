#!/usr/bin/python3
"""
Module of a function to fetch a TODOlist of all employees and
 export them to a json file "todo_all_employees.json"
"""
import json
import requests


def export_todos():
    """
    Fetches employees todo lists and exports them
    """
    json_data = {}
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    employees_list = response.json()
    if (type(employees_list) is not list):
        return
    for employee in employees_list:
        employee_id = employee.get("id")
        employee_alias = employee.get("username")

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
        json_data[employee_id] = todo_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    export_todos()
