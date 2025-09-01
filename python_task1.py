tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nYou have no tasks right now.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter a new task: ").strip()
    if task != "":
        tasks.append(task)
        print(f"'{task}' has been added to your list!")
    else:
        print("Task cannot be empty!")

def remove_task():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("\nWhich task do you want to remove? Enter the number: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"'{removed}' has been removed from your list!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("What would you like to do? (1/2/3/4): ").strip()

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Bye! Have a great day!")
        break
    else:
        print("Invalid choice! Please try again.")