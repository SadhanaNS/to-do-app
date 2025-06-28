from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)

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
