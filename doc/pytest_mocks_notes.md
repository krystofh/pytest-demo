
# **Mocks**

This chapter provides an overview of using **pytest mocks** for testing functions that interact with external services like APIs. Mocking allows you to simulate server responses without making actual network calls, making tests faster, more reliable, and independent of external factors.

---

## **1. Why Use Mocks?**

- Avoids making real network requests, which can be slow or unreliable.
- Simulates various responses (e.g., success, failure, exceptions).
- Isolates the code under test by replacing external dependencies.

---

## **2. Mocking with `@mock.patch`**

The `@mock.patch` decorator is used to replace a function (e.g., `requests.get`) with a mock during the test. This allows you to control its behavior.

### **Example: Mocking a Server Response**
```python
import unittest.mock as mock
from source import service

@mock.patch("requests.get")
def test_todo_mocked(mock_get):
    mock_response = mock.Mock()  # Create a mock object
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            "userId": 1,
            "id": 1,
            "title": "prepare the tutorial",
            "completed": False,
        },
    ]
    mock_get.return_value = mock_response  # Mock requests.get's return value

    data = service.get_todos()  # Call the function under test

    assert type(data) == list
    assert list(data[0].keys()) == ["userId", "id", "title", "completed"]
```

### **Key Points:**
1. **`@mock.patch("requests.get")`**:
   - Replaces `requests.get` with a mock object during the test.
2. **`mock_response.json.return_value`**:
   - Simulates the `json()` method's return value on a real `requests.Response`.
3. **Control Behavior**:
   - By setting `mock_get.return_value`, you can dictate how `requests.get` behaves in your tests.

---

## **3. Mocking Exceptions**

You can simulate errors like `TypeError`, `HTTPError`, or custom exceptions using mocks. This ensures your code handles errors gracefully.

### **Example: Testing a TypeError**
```python
import pytest
import unittest.mock as mock
from source import service

@mock.patch("requests.get")
def test_todo_mocked_typeerror(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    # Simulate an unexpected response structure
    mock_response.json.return_value = {
        "userId": 1,
        "id": 1,
        "title": "prepare the tutorial",
        "completed": False,
    }
    mock_get.return_value = mock_response

    with pytest.raises(TypeError):
        service.get_todos()
```

### **Key Points:**
1. **Custom Response**:
   - The response is mocked as a dictionary instead of a list.
2. **Error Handling**:
   - Use `pytest.raises` to assert that a specific exception is raised.

---

## **4. Mocking Lifecycle**

Mocking affects only the duration of the test. After the test:
- The mocked function (e.g., `requests.get`) returns to its original behavior.
- This ensures isolation between tests.

---

## **5. Summary of Mocking Workflow**

1. **Create a Mock Object**:
   - `mock.Mock()`: Simulates the behavior of the object being mocked.
2. **Control the Mock**:
   - Use `.return_value` to specify the result of the mock method.
3. **Patch the Function**:
   - Replace the target function using `@mock.patch`.
4. **Test Your Code**:
   - Call the function under test and verify its behavior against the mocked response.

---

### **Snippet: Real Request vs. Mocked Response**
```python
# Real request
data = service.get_todos()
assert len(data) > 0

# Mocked request
@mock.patch("requests.get")
def test_mocked(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"userId": 1, "id": 1, "title": "task", "completed": False}]
    mock_get.return_value = mock_response

    data = service.get_todos()
    assert len(data) > 0
```

---

## **6. Best Practices**

- **Scope Mocks Precisely**:
  - Use `@mock.patch` for specific functions (e.g., `requests.get`).
- **Test All Scenarios**:
  - Simulate success, failure, and edge cases (e.g., empty responses, timeouts).
- **Clean Assertions**:
  - Ensure tests focus on relevant behavior without over-complicating checks.

By mastering pytest mocks, you can create robust, isolated, and fast tests for functions that depend on external services.
