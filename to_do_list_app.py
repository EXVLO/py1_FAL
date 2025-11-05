import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!\n")
    else:
        print("Task cannot be empty!\n")

def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: "))
        removed = tasks.pop(index - 1)
        print(f"Removed task: {removed}\n")
    except (ValueError, IndexError):
        print("Invalid number!\n")

def main():
    tasks = load_tasks()
    # print(os.path.abspath("tasks.txt"))
    while True:
        print("=== TO-DO LIST ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice, try again!\n")

if __name__ == "__main__":
    main()
