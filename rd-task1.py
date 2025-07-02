# RD-INFRO-TECHNOLOGY-
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['description']}")

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added.")

def update_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_desc = input("Enter new description: ")
            tasks[index]["description"] = new_desc
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to toggle complete/incomplete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = not tasks[index]["completed"]
            save_tasks(tasks)
            print("Task status updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Show Tasks\n2. Add Task\n3. Update Task\n4. Mark Complete/Incomplete\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
