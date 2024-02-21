#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(api_url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get("title") for t in tasks if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]
