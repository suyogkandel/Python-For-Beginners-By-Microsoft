def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name:')
first_name_initial = get_initial(first_name)#

middle_name = input('Enter your middle name:')
middle_name_initial = get_initial(middle_name, False)#

last_name = input('Enter your last name:')
last_name_initial = get_initial(force_uppercase=True, name=last_name)#

print('Your initials are: ' + first_name_initial + middle_name_initial + last_name_initial) 