#!/usr/bin/env python3
"""
File: service.py
Author: krystofh
Date: 2024-12-03
Description: Create a request to API and get some data
"""

import requests


def get_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code == 200:
        # Raise TypeError if the data is not packed in a list
        if type(response.json()) != list:
            raise TypeError
        return response.json()
    raise requests.HTTPError
