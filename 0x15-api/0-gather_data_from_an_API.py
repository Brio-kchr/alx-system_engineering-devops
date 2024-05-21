#!/usr/bin/python3
"""
Module of a function to fetch a TODOlist progress of an
 employee from jsonplaceholder
"""
import requests


def print_todo_progress(employee_id: int):
    """
    Fetches employee todo list progress and prints it
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".
        format(employee_id)
    )
    employee_name = response.json()
    if (type(employee_name) is not list) or (len(employee_name) < 1):
        return
    employee_name = employee_name[0].get("name")

    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )
    todo_list = response.json()
    done_tasks = [task for task in todo_list if task["completed"]]
    print(
        "Employee {} is done with tasks({}/{}):"
        .format(employee_name, len(done_tasks), len(todo_list))
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    from sys import argv

    print_todo_progress(argv[1])
