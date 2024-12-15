from flask import Flask, request, redirect, url_for, render_template_string
import random

app = Flask(__name__)

tasks = [] # Keep the task list in memory

RANDOM_DESCRIPTIONS = [
    "Eat a sentient pickle",
    "Dance with a cactus",
    "Solve the mysteries of socks",
    "Learn to speak dolphin",
    "Befriend a squirrel with a tiny hat",
    "Sing opera to a toaster",
    "Convince a cat to do taxes",
    "Build a fort of bananas",
    "Measure the length of a dream",
    "Invent a new flavor of air"
]

def generate_task_list_html():
    bg_color = f"#{random.randint(0, 0xFFFFFF):06x}" #random hex color
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Chaotic Task Manager</title>
        <style>
        body {{
            background-color: {bg_color};
            font-family: 'Comic Sans MS', cursive;
            padding: 20px;
        }}
         h1 {{
            color: purple;
            text-shadow: 2px 2px 4px #000000;
            }}
        ul {{
            list-style-type: none;
        }}
        </style>
    </head>
    <body>
        <h1>Task Manager of Randomness</h1>
         <form action="/add_task" method="post">
            <input type="text" name="task" placeholder="Add a normal task... or maybe not" style="margin-bottom: 10px;">
           <button type="submit" style="background-color: lightblue; padding: 8px; border-radius:5px; border: none;">Add Task</button>
        </form>
        <h2>Tasks: Probably Important, Probably Not</h2>
    <ul>
    """
    for index, task in enumerate(tasks):
      html += "<li>\n"
      if task["completed"]:
          html += f"<span style='text-decoration: line-through;'>{task['description']}</span>\n"
      else:
        html += f"{task['description']}\n"
      if not task["completed"]:
         html += f"<form action='/complete_task/{index}' method='post' style='display: inline;'>\n"
         html += "<button type='submit' style='background-color: lightgreen; border: none; padding:5px; border-radius: 5px;'>Mark Complete</button>\n"
         html += "</form>\n"
      html += f"<form action='/delete_task/{index}' method='post' style='display: inline;'>\n"
      html += "<button type='submit' style='background-color: lightcoral; border:none; padding: 5px; border-radius: 5px;'>Delete</button>\n"
      html += "</form>\n"
      html += "</li>\n"
    html += "</ul></body></html>"
    return html


@app.route("/")
def index():
    return generate_task_list_html()

@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if not task or random.random() < 0.4:  # 40% chance of random task
        task = random.choice(RANDOM_DESCRIPTIONS)
    tasks.append({"description": task, "completed": False})
    return redirect(url_for("index"))

@app.route("/complete_task/<int:task_index>", methods=["POST"])
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
       if random.random() < 0.3:  # 30% chance of chaos
        tasks[task_index]["description"] = "Task completed... or maybe it ate your socks?"
       else:
        tasks[task_index]["completed"] = True
    return redirect(url_for("index"))


@app.route("/delete_task/<int:task_index>", methods=["POST"])
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
      if random.random() < 0.5:
        tasks.insert(random.randint(0, len(tasks)), {"description": "A new task appeared from nowhere!", "completed": False})
      else:
         tasks.pop(task_index)

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)