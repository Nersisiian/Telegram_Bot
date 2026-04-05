import json, os

TASK_FILE = "data/tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return {}
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task(user_id, task):
    tasks = load_tasks()
    tasks.setdefault(str(user_id), []).append(task)
    save_tasks(tasks)

def list_tasks(user_id):
    tasks = load_tasks()
    return tasks.get(str(user_id), [])

def delete_task(user_id, index):
    tasks = load_tasks()
    if str(user_id) in tasks and 0 <= index < len(tasks[str(user_id)]):
        tasks[str(user_id)].pop(index)
        save_tasks(tasks)
        return True
    return False
