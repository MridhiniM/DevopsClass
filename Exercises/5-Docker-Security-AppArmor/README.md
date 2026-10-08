# Exercise 5: Docker Security with AppArmor and Python

## Objective

The objective of this exercise is to secure a Dockerized Flask application using an AppArmor security profile and Python's Docker SDK.

The exercise demonstrates how container security policies can restrict access to sensitive files, directories, capabilities, and executable files.

> **Environment Note:** This exercise was performed on macOS using Docker Desktop. Docker Desktop runs containers inside a Linux VM, but AppArmor was not available in the Docker Desktop environment used for this exercise. Therefore, the AppArmor profile was created and inspected, but could not be loaded or enforced.

---

## 1. Flask Application

The Flask application returns a simple message when accessed.

### `app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a secure Flask application running inside a Docker container!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
