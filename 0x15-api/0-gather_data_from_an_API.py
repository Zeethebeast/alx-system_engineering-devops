#!/usr/bin/env python3
"""
Fetches and prints completed TODO tasks for a specified user from JSONPlaceholder API.
"""

import sys
import requests

def main():
    """Fetch and print TODO tasks for the specified user."""
    # Check if an argument was provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <user_id>")
        sys.exit(1)

    # Get the user ID from the command-line arguments
    user_id = sys.argv[1]

    # Get the TODO items for the specified user
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Get the user details for the specified user
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(user_url)
    user = response.json()
    user_name = user['name']

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed = len(completed_tasks)
    num_total = len(todos)

    # Print employee's completed tasks
    print(f"Employee {user_name} is done with tasks({num_completed}/{num_total}):")
    for todo in completed_tasks:
        print(f"\t {todo['title']}")

if __name__ == "__main__":
    main()

