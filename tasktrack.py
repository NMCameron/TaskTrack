"""A command-line task manager created for CPS 310.

Author: Cameron Nebel
Course: CPS 310
"""
TASKS_FILE = "tasks.txt"



def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")



def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""
    task = input("Enter a new task: ").strip()
    if not task:
        print("A task cannot be empty.")
    else:
        tasks.append(task)
        print("Task added successfully.")



def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")



def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""
    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        # A new project may not have a task file yet.
        return []

    return tasks



def save_tasks(tasks, filename):
    """Save all tasks to a text file."""
    with open(filename, "w") as file:
        for task in tasks:
                file.write(f"{task}\n")



def remove_task_by_number(tasks, task_number):
    """Remove a task by its displayed number and return the removed task.

    Return None when the task number is outside the valid range.
    """
    #TODO: Validate the task number.
    #TODO: Remove and return the selected task.

    if task_number <= 0 or task_number > len(tasks):
        return None

    return tasks.pop(task_number - 1)



def remove_task(tasks):
    """
    Prompt the user to select and remove a task.
    Return True when a task is removed and False otherwise.
    """
    if not tasks:
        print("No tasks are available to remove.")
        return False

    view_tasks(tasks)
    selection = input("Enter the number of the task to remove: ").strip()
    if not selection.isdigit():
        print("Error. Please enter a number.")
        return False
    
    task_number = int(selection)

    removed_task = remove_task_by_number(tasks, task_number)

    if removed_task is None:
        print("Error. Task does not exist.")
        return False

    print(f"Successfully removed {task_number}. {removed_task}")
    return True



def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks, TASKS_FILE)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid selection.\nPlease pick an option 1-4.")



if __name__ == "__main__":
    main()