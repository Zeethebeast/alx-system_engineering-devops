#!/usr/bin/python3
"""
Fetches and exports todo tasks for a specified user from JSONPlaceholder API to a CSV file.
"""
import csv
import requests
import sys

def main():
    """Fetch and export todo tasks for the specified user."""
    # Check if an argument was provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <user_id>")
        sys.exit(1)

    # Get the user ID from the command-line arguments
    user_id = sys.argv[1]

    try:
        # Get the user details for the specified user
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Check for HTTP errors
        user = user_response.json()
        user_name = user['name']

        # Get the todo items for the specified user
        todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()  # Check for HTTP errors
        todos = todos_response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    # Prepare data for writing to CSV
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        # Write the header with the required format (optional)
        csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write each task's details to the CSV file
        for todo in todos:
            csvwriter.writerow([user_id, user_name, todo['completed'], todo['title']])

    # Print confirmation
    print(f"Data for user {user_name} (ID: {user_id}) has been exported to {csv_filename}.")

if __name__ == "__main__":
    main()

