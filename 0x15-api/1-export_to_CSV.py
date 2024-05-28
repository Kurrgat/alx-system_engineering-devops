#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import csv
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

    # CSV filename
    filename = f"{employee_id}.csv"

    # Write to CSV
    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csvwriter.writerow([employee_id, username, task.get("completed"), task.get("title")])

    print(f"Data exported to {filename}")
