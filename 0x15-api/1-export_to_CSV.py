#!/usr/bin/env python3
import sys
import requests
import csv
"""
Fetches and prints completed TODO tasks for a specified user from JSONPlaceholder API.
"""
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

# Prepare data for writing to CSV
csv_filename = f"{user_id}.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header with the required format
    csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
    # Write each task's details to the CSV file
    for todo in todos:
        csvwriter.writerow([user_id, user_name, todo['completed'], todo['title']])

# Print confirmation
print(f"Data for user {user_name} (ID: {user_id}) has been exported to {csv_filename}.")
