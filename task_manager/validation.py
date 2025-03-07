# This module is responsible for validating user input
# We will print out a message IFF validation fails
# Note: having task_utils call this instead of main makes the UX worse

from datetime import datetime

# A valid title must contain some non-space character(s)
def validate_task_title(title):
    if len(title.strip()) == 0:
        print("Title cannot be empty.")
        return False
    return True
    
# The length of the description must be less than a million characters
def validate_task_description(description):
    if len(description) > 1_000_000:
        print("Description must be less than one million characters.")
        return False
    return True
    
DATE_FORMAT = "%Y-%m-%d"
# Use the datetime library to verify the date in the specified format
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, DATE_FORMAT)
        return True
    except:
        print(f"Date must be formatted as 'YYYY-MM-DD' - could not parse {due_date}")
        return False
    