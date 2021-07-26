# Defining a function for UI
def userInterface():
    print('###############################')
    print('MYPY PHONE BOOK')
    print('###############################')
    print('1 : Add New Entry')
    print('2 : Delete Entry')
    print('3 : Update Entry')
    print('4 : Lookup Number')
    print('5 : QUIT')

# we declare blank dictionary
phone_book = {}

# while executing tasks, creating a variable for receiving user input
select_option = 0

# Add a contact number to the phone book dictionary with this function.
def add_contact_number():
    full_name = input('Enter Full Name : ')
    while True:
        try:
            contact_num = int(input('Enter Contact Number : '))
            break
        except ValueError:
            print("Invalid Contact Number Entered")

    contact_exists = 0
    full_name_exists = 0
    flag = True

    '''
    Checking to see if a contact number already exists If the number is present, it will display the message. 
    Contact Number Already Exists" and the cycle will continue. If not present, it will check if an entry with 
    the supplied name already exists and increase the value of the variable by one.
    '''
    for stored_full_name, stored_contact_num in phone_book.items():
        if contact_num in stored_contact_num:
            print("Contact Number already present")
            contact_exists += 1
            break
        elif full_name == stored_full_name:
            full_name_exists += 1

    '''
    Adding several numbers for a single individual If an item with the Full Name already exists, it will add the
    new contact number to that record; otherwise, it will create a new entry in the dictionary with the Full Name 
    as the key and the entered number in list format.
    '''
    if full_name_exists >= 1:
        phone_book[full_name].append(contact_num)
        print("Contact Number Added")
    elif contact_exists == 0:
        phone_book[full_name] = [contact_num]
        print("Contact Number Added")

# to carry out phone book operations
while select_option!=5:
    userInterface()
    try:
        select_option = int(input())
        if (select_option not in range(1,6)):
            print("Please check value entered ! ")
            continue
    except ValueError:
        print("Please check value entered ! ")
        continue

    ## Add New Entry ##
    if select_option == 1:
        add_contact_number()

    elif select_option == 2:
        '''
        If there is no data in the dictionary, the message below will be shown, and the loop will continue. 
        Otherwise, it will prompt you to input full name, which must be removed.
        '''
        if len(phone_book.keys()) == 0:
            print('No data exist')
            continue
        else:
            full_name = input("Enter Name to Delete from Phone Book : ")

        '''
        If a complete name is found in the phone book, it will verify how many contact numbers are associated with 
        that full name; if there is only one, the entry will be removed from the phone book. Otherwise, it will display 
        all accessible phone numbers for that complete name and prompt you to choose which one you want to remove.
        '''
        if full_name in phone_book:
            if len(phone_book[full_name]) > 1:
                print(f"You have below contact number for {full_name}\n"
                      f"Please select a number which you want to delete")

                for i in range(len(phone_book[full_name])):
                    print(f"{i + 1} - {phone_book[full_name][i]}")

                while True:
                    try:
                        delete = int(input(f"Please enter a number from 1 - {len(phone_book[full_name])} : "))
                        if(delete not in range(1,len(phone_book[full_name])+1)):
                            print("Invalid Input !\nPlease check again.")
                            continue
                        else:
                            '''
                            It will remove/pop the contact number at the chosen index if there are several contact numbers 
                            for the same complete name.
                            '''
                            phone_book[full_name].pop(delete-1)
                            break
                    except:
                        pass
            else:
                phone_book.pop(full_name)

            print("Contact Deleted !")
        else:
            print("Invalid Full Name! Please check again")

    elif select_option == 3:
        '''
        This function is used to avoid updating duplicate contact numbers because we don't know if the
        contact that has to be changed has only one or several contact numbers. As a result, to accommodate 
        multiple arguments, *args is utilized.
        '''
        def get_new_number(*args):
            try:
                ner_number = int(input("Please enter New Number : "))
            except ValueError:
                print("Invalid Number !")
                return False
            else:
                flag = True
                for i in phone_book.values():
                    if ner_number in i:
                        flag = False
                if flag:
                    if (len(args) == 1):
                        phone_book[args[0]] = [ner_number]
                    else:
                        phone_book[args[0]][args[1]] = ner_number
                else:
                    print("Entered Number already present !\nContact Number not updated.")
                    return False

        if len(phone_book.keys()) == 0:
            print('No data present')
            continue
        else:
            full_name = input("Enter Name to Update in phone_book : ")

        if full_name in phone_book.keys():
            if len(phone_book[full_name]) > 1:
                print(f"You have below contact number for {full_name}\n"
                      f"Please select a number which you want to update")
                for i in range(len(phone_book[full_name])):
                    print(f"{i + 1} - {phone_book[full_name][i]}")

                while True:
                    try:
                        update = int(input(f"Please enter a number from 1 - {len(phone_book[full_name])} : "))
                        if (update not in range(1, len(phone_book[full_name]) + 1)):
                            print("Invalid Input !\nPlease check again.")
                            continue
                        else:
                            if(get_new_number(full_name,i)):
                                print("Contact Updated !")
                    except:
                        pass
            else:
                if (get_new_number(full_name)):
                    print("Contact Updated !")
        else:
            print("Invalid full_name! Please check again")

    elif select_option == 4:

        if len(phone_book.keys()) == 0:
            print('No data present')
            continue

        look_up_found = 0
        while look_up_found == 0:
            try:
                lookup = int(input("Please enter a number : "))
            except ValueError:
                print("Invalid Number ! Please try Again.")
                continue
            else:
                # Display Full name for entered contact number
                for name,contact_nums in phone_book.items():
                    if lookup in contact_nums:
                        print(f"Contact Number Found\n"
                              f"Full Name : {name}\n"
                              f"Contact Number : {lookup}")
                        look_up_found += 1

                # If Contact number does not exists asks to add new one 
                if look_up_found == 0:
                    toAdd = input("Contact Number not found in Phone Book. Do you want to add it.\n"
                                  "Press 'y' if yes, any other Key to exit : ")
                    if toAdd.lower() == 'y':
                        add_contact_number()
                        break
                    else:
                        break