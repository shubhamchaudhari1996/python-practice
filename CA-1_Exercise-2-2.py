import re

# UI Layout
print('###############################')
print('WELCOME TO THE DBS CONSOLE')
print('###############################')

# Validation while taking a input from user in given format
while True:
    user_name = input('Please enter your User Name: ')
    if not re.match('^[a-zA-Z]*\\\\[0-9]*$', user_name):
        print('Invalid format, Please enter Domain\\User Name')
        continue
    else:
        break

# Spliting the User Name by \
split_string = user_name.split('\\')

# storing the user_name in upper case after Spliting
convertedList = [x.upper() for x in split_string]

# printing the doamin and user_name
print('\nDomain : ',convertedList[0])
print('User Name : ',convertedList[1])