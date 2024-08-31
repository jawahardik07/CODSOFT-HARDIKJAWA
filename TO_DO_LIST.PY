import json

# File to store tasks
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    description = input("Enter the task description: ")
    task = {"description": description, "status": "incomplete"}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# Update an existing task
def update_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]["description"] = input("Enter the new task description: ")
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Mark a task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]["status"] = "complete"
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    
    print("\nTo-Do List:")
    for index, task in enumerate(tasks):
        status = "✓" if task["status"] == "complete" else "✗"
        print(f"{index + 1}. {task['description']} [{status}]")
    print()

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a new task")
        print("3. Update a task")
        print("4. Mark a task as complete")
        print("5. Delete a task")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_task_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

