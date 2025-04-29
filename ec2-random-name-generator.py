import random
import string

# Obtain user input for the number of instances
ec2_number = int(input("Enter the number of EC2 intances: "))
if ec2_number < 1:
    print("The number of instances.")

# Generate the department names 
department_name = input('Enter your department name. ')
valid_departments = ("Marketing", "Accounting", "FinOps")

# Get user input for department name
if not valid_departments:
    print('You cannot use name generator!')
else:
    print('You have access to name generator!') 

# Generate unique names
def generate_unique_names(department_name):
    # Generate random string
    for i in range(ec2_number):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return random_string
    print(generate_unique_names)

