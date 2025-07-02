from flask import Flask, request, redirect, render_template_string
import os
import requests  # vulnerable if old version is used (CVE-2018-18074)

app = Flask(__name__)

# 🔐 Hardcoded Secret for secret scanning
API_KEY = sk_live_51HXZrHAp0qhKZq9Ld2FB9HzRj3kIqI4fzRZjYbUBxDeqbLfj3kIqI
Connection_Strings = Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=myPassword
API_Keys = AKIAIOSFODNN7EXAMPLE
Private_Keys =  "-----BEGIN PRIVATE KEY-----"
Connection_Strings = "Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=myPassword"
HTTP_Authentication_Headers =  "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ="
Passwords =  "password123"

# ⚠️ Insecure function to simulate command injection vulnerability
def run_shell_command(cmd):
    os.system(cmd)  # Insecure usage (for CodeQL scan)

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>To-Do List</title></head>
<body>
    <h1>My To-Do List</h1>
    <form method="POST" action="/add">
        <input type="text" name="task" required>
        <input type="submit" value="Add Task">
    </form>
    <ul>
        {% for task in tasks %}
        <li>{{ task }} <a href="/delete/{{ loop.index0 }}">❌</a></li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")

    # Optional: Trigger command injection simulation
    run_shell_command(f"echo Adding task: {task}")  # CodeQL test

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
