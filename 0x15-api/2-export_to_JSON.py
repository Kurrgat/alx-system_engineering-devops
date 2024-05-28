#!/usr/bin/python3
"""Exports data in JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    
    # Fetch employee details
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch employee's todo list
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # JSON filename
    filename = f"{employee_id}.json"

    # Prepare data for JSON
    tasks_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    # Create the JSON object
    json_data = {str(employee_id): tasks_list}

    # Write to JSON file
    with open(filename, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"Data exported to {filename}")
