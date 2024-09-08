def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: "))
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task removed successfully!")
    else:
        print("Invalid index.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def mark_task_completed(tasks):
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(tasks):
        tasks[task_index] = f"✅ {tasks[task_index]}"
        print("Task marked as completed.")
    else:
        print("Invalid index.")

def main():
    tasks = []
    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Mark task as completed")
        print("5. Quit")
        choice = int(input())

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            remove_task(tasks)
        elif choice == 3:
            display_tasks(tasks)
        elif choice == 4:
            mark_task_completed(tasks)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()