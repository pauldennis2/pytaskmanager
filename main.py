# This is a Task Management app.
# This module is responsible for handling the CLI
from task_utils import *

def print_menu():
    print("Task Management System")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. View Progress")
    print("5. Exit")

# Main function manages user I/O
# Turns over actual logic to task_utils
def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("What is the title of your task? (Cannot be empty)")
            title = input()
            print("Enter a description (optional)")
            description = input()
            print("Enter the due date formatted as 'YYYY-MM-DD'")
            date = input()
            add_task(title, description, date)
            None
        elif choice == "2":
            print("What task number should be marked as done?")
            index = int(input())
            mark_task_as_complete(index - 1) #Subtract 1 to turn human readable index to 0-index
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            rounded_progress = round(calculate_progress(), 2)
            print(f"Your progress is: {rounded_progress}")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
