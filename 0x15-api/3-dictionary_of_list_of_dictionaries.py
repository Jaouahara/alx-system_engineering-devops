#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(api_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            emp.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": emp.get("username")
            } for t in requests.get(api_url + "todos",
                                    params={"userId": emp.get("id")}).json()]
            for emp in employees}, jsonfile)
