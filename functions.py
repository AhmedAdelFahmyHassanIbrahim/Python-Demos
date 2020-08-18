from datetime import datetime


#this is a functions current date and time 
#custom messages
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = "Ahmed"
# print_time("task is done")

# for x in range(0, 10):
#     print(x)

# print_time("Task is done")



def get_initial(name, force_uppercase = True):
    if force_uppercase:
        initial = name[0:1].upper
    else:
        initial = name[0:1]
    return initial


first_name = input("Enter your first name: ")
first_name_initial = get_initial(force_uppercase = False, name = first_name)

last_name = input("Enter your last name: ")
last_name_initial = get_initial(name = last_name, force_uppercase = True)

print('Your initials are: ' + first_name_initial + ' ' + last_name_initial)