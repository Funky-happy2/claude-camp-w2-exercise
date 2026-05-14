# Print the past list of tasks from the file even if the file is not there, it will not cause an error
print("Your current to-do list:")
tasks = []
try:
    with open("to_do_list.txt", "r") as file:
        tasks = file.readlines()
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")
except FileNotFoundError:
    print("No to-do list found.")

# Create loop that continues until the user wants to exit
while True:
    # Ask user whether to add a task or delete a task
    action = input("Would you like to add a task or delete a task? (type 'add' to add, 'delete' to delete, or 'exit' to quit): ")
    if action.lower() == 'add':
        # Ask the user for a task
        task = input("Enter a task to add to your to-do list (or type 'exit' to quit): ")
        # Add the task to the file
        file = open("to_do_list.txt", "a")
        file.write(task + "\n")
        file.close()
        print(f"Task '{task}' has been added to your to-do list.")

    # Check if the user wants to exit
    elif action.lower() == 'exit':
        print("Exiting the to-do list application. Goodbye!")
        break

    elif action.lower() == 'delete':
        # Ask the user for the number of the task to delete
        try:
            task_number = int(input("Enter the number of the task you want to delete (or type '0' to cancel): "))
            if task_number == 0:
                print("Deletion cancelled.")
                continue
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1).strip()
                with open("to_do_list.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Task '{deleted_task}' has been deleted from your to-do list.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
# After exiting the loop, display the to-do list
print("\nYour To-Do List:")
with open("to_do_list.txt", "r") as file:
    tasks = file.readlines()
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task.strip()}")