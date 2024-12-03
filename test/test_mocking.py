#!/usr/bin/env python3
"""
File: test_mocking.py
Author: krystofh
Date: 2024-12-03
Description: This test file demonstrates using actual request command and then mocking server response. The mocked response is then checked.
"""

import pytest
import unittest.mock as mock
from source import service


# Send actual request and test the response
def test_get_todos():
    data = service.get_todos()  # get data using real request
    assert len(data) > 0
    # check that the keys of the entries are as expected
    assert list(data[0].keys()) == ["userId", "id", "title", "completed"]
    assert type(data[0]["userId"]) == int
    assert type(data[0]["id"]) == int
    assert type(data[0]["title"]) == str
    assert type(data[0]["completed"]) == bool


# ------- Use mocking instead of request --------------------------------
# mock request command in the function call service.get_todos()
@mock.patch("requests.get")
# the patched command is named "mock_get"
def test_todo_mocked(mock_get):
    mock_response = mock.Mock()  # create a mock object
    # Create mocked server response which would be obtained by the patched command
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "userId": 1,
            "id": 1,
            "title": "prepare the tutorial",
            "completed": False,
        },
        {
            "userId": 2,
            "id": 2,
            "title": "publish this tutorial to github",
            "completed": False,
        },
    ]
    # calling mock_get (requests.get) returns value assigned by .return_value
    mock_get.return_value = mock_response
    # Call the actual function being tested, the command "requests.get" is replaced by the patch
    data = service.get_todos()
    # check that the keys of the entries are as expected
    assert type(data) == list
    assert list(data[0].keys()) == ["userId", "id", "title", "completed"]
    assert type(data[0]["userId"]) == int
    assert type(data[0]["id"]) == int
    assert type(data[0]["title"]) == str
    assert type(data[0]["completed"]) == bool


# Demonstrate raising exceptions as expected
@mock.patch("requests.get")
# @pytest.mark.xfail(reason="Testing return value as dict instead of list")
def test_todo_mocked_typeerror(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    # Pack the response as a dict with single entry instead of list like [{"userId": ...}]
    mock_response.json.return_value = {
        "userId": 1,
        "id": 1,
        "title": "prepare the tutorial",
        "completed": False,
    }
    mock_get.return_value = mock_response
    # Check that TypeError is being raised
    with pytest.raises(TypeError):
        data = service.get_todos()
