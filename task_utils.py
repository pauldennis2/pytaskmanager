# This module does the actual "work" of managing tasks
#
# This is the structure of a task:
# task = {"title": "Groceries",
#  "description": "Shop at Market Basket for food", 
#  "due_date": "2024-06-26",
#  "completed": True}

from validation import *

# Define tasks list
tasks = [{"title": "Conquer Normandy", "description": "RARRRRGH!", "due_date": "1099-04-30", "completed": True},
         {"title": "Watch Star Trek TNG", "description": "Darmok", "due_date": "2005-01-31", "completed": False},
         {"title": "Build my own spaceship", "description": "", "due_date": "2025-12-31", "completed": False}]

# After validating the inputs, add the task to our list
def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        new_task = {"title": title, "description": description, "due_date": due_date, "completed": False}
        tasks.append(new_task)
        print("Task added successfully!")
    else:
        print("Could not add task")
    
# Mark a task as complete using the index of the task
# No behavior change if task is already complete
def mark_task_as_complete(index, tasks=tasks):
    if index < 0:
        print("Negative indexing not allowed.")
        return
    if index >= len(tasks):
        print(f"Index is too high. Only {len(tasks)} tasks in list.")
        return
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Print pending tasks
# We will add a not necessarily sequential "human readable" index
def view_pending_tasks(tasks=tasks):
    if not tasks: #If tasks is empty
        print("There are no tasks in the list")
        return
    print("Pending Tasks (indexes non-sequential because of completed tasks)")
    index = 1
    for task in tasks:
        if not task["completed"]:
            print(f"{index}. {task}")
        index += 1 #Increment regardless of whether task was complete or not

# This function should return the percentage of tasks complete times 100
# For example 50% completed should return 50 (not 0.5)
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    tasks_complete = 0
    for task in tasks:
        if task["completed"]:
            tasks_complete += 1

    return (tasks_complete / len(tasks)) * 100
