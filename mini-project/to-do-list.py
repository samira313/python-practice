# Simple To-Do List App

# Define an empty list to store tasks
tasks = []

# Show menu until user chooses to exit
while True:
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        # Show all current tasks
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        # Add a new task
        new_task = input("Enter your new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added!")

    elif choice == "3":
        # Remove a task by number
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                remove_index = int(input("Enter the task number to remove: "))
                if 1 <= remove_index <= len(tasks):
                    removed = tasks.pop(remove_index - 1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        # Exit the app
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")
