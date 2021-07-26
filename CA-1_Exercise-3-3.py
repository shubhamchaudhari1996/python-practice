# UI layout
print('###############################')
print('WELCOME TO THE DBS CONSOLE')
print('###############################')

# Input from user to define a Length of list
len = int(input('Input the number of elements sorted in the list: '))
print('Input',Length,'elements in the list: ')
list = []

# Adding values to the list
for i in  range(len):
        list.append(input(f"element - {i} : "))

print('\n')
# Finding occurances
for j in set(list):
        print(j,' Occurs ',list.count(j),' times')