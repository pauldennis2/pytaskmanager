from datetime import datetime

#A valid title must contain some non-space character(s)
def validate_task_title(title):
    return not len(title.strip()) == 0
    
#Since we have no fixed size box, any description including empty is allowed
def validate_task_description(description):
    return True
    
DATE_FORMAT = "%Y-%m-%d"
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, DATE_FORMAT)
        return True
    except:
        print(f"Date must be formatted as 'YYYY-MM-DD' - could not parse {due_date}")
        return False


print(validate_due_date("1999-99-20"))
print(validate_due_date("2056-03-05"))
print(validate_due_date("1995-02-30"))
print(validate_due_date("2000-02-29"))

print(validate_due_date("2001-02-29"))
