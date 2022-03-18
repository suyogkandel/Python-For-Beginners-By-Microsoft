# Import the datetime class from datetime library
from datetime import datetime
# Print the correct time
def print_time(task_name):#function definition
    print(task_name)
    print(datetime.now())
    print()
print_time('date & time')#function call

for x in range(0,10):
    print(x)
print_time('loop completed')#function call