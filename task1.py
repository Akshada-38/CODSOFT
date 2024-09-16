# Simple To-Do List in Python (Command-line Interface)

tasks = []

def show_menu():
    print("#---------------------------------------------#\n")
    print("      ||       To-Do List Menu:     ||      ")
    print("#-----------------------------------------------#")
    print("                   1. View To-Do List           ")
    print("                   2. Add Task")
    print("                   3. Update Task")
    print("                   4. Delete Task")
    print("                   5. Exit")
    print("#------------------------------------------------#")

def view_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list!")

def update_task():
    view_tasks()
    task_number = int(input("\nEnter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Enter the updated task: ")
        tasks[task_number] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def delete_task():
    view_tasks()
    task_number = int(input("\nEnter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task}' deleted!")
    else:
        print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")
       
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()