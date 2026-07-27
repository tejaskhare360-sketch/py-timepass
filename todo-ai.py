import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def show_tasks(tasks):
    print("\n===== MY TO DO LIST =====")
    if not tasks:
        print("  (no tasks yet)")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        print(f"  {i}. [{status}] {task['name']}")
    print("=========================\n")

def add_task(tasks):
    name = input("Enter task name: ").strip()
    if name:
        tasks.append({"name": name, "done": False})
        save_tasks(tasks)
        print(f'✅ Task "{name}" added!')
    else:
        print("⚠️  Task name cannot be empty.")

def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f'✅ Task "{tasks[num - 1]["name"]}" marked as done!')
        else:
            print("⚠️  Invalid number.")
    except ValueError:
        print("⚠️  Please enter a number.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f'🗑️  Task "{removed["name"]}" deleted!')
        else:
            print("⚠️  Invalid number.")
    except ValueError:
        print("⚠️  Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nWhat do you want to do?")
        print("  1. View tasks")
        print("  2. Add a task")
        print("  3. Mark task as done")
        print("  4. Delete a task")
        print("  5. Quit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋Goodbye!")
            break
        else:
            print("⚠️  Please choose 1 to 5.")

main()
