from Classes import Record
from support_funcs import split_data
from support_funcs import phone_validator


def add_func(data: str, book):
    """Adding contact to the address book"""

    name, phone = split_data(data)

    if name not in book.data.keys() and not phone:
        new_contact = Record(name)
        book.add_record(new_contact)
        print('\n\033[31m!!! The phone number is not specified.\n!!! Or is specified in the wrong format.\033[0m')
        return book, f'\n<<< New contact has been added:\n[{name}]:[\033[31m\033[1m\033[4mNo number available\033[0m]\n'
    elif name not in book.data.keys() and phone:
        new_contact = Record(name, phone)
        book.add_record(new_contact)
        return book, f'\n<<< New contact has been added:\n[{name}]:[{phone}]\n'

    contact = book.data[name]
    if contact.has_phone(phone):
        return book, f'<<< This phone number already exists!'
    elif not contact.has_phone(phone) and phone:
        contact.add_phone(phone)
        return book, f'\n<<< Number [{phone}] has been added to contact: [{name}]\n'
    else:
        return book, '\n<<< This contact already exists!\n'


def change_phone_func(data: str, book):
    """Changing an existing contact number"""
    name, phone_old = split_data(data)

    if name in book.data.keys():
        contact = book.data[name]
        if contact.has_phone(phone_old):
            phone_new = input('Please enter new phone number: ')
            phone_new = phone_validator(phone_new)
            contact.change_phone(phone_old, phone_new)
            return book, f'\n<<< The contact number has been changed from:\n[{phone_old}] to [{phone_new}]\n'
        else:
            return book, f"\n<<< This phone number doesn't exist!"
    else:
        return book, "<<< This contact doesn't exist!"


def del_func(data: str, book):
    """Deleting contact to the address book"""
    name, phone = split_data(data)
    if name not in book.data.keys():
        return book, f'\n<<< Contact with name [{name}] not found!\n'
    contact = book.data[name]
    if not phone:
        confirmation = input(f'\033[33mDo you want to delete contact [{name}] completely?\033[0m Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            book.del_record(name)
            return book, f'\n<<< Contact [{name}] has been deleted!!!\n'
        else:
            return book, '\n<<< Abolition...\n'
    elif contact.has_phone(phone):
        confirmation = input(f'\033[33mDo you want to delete phone [{phone}]?\033[0m Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            contact.del_phone(phone)
            return book, f'\n<<< Number [{phone}] has been deleted from [{name}]\n'
        else:
            return book, '\n<<< Abolition...\n'
    else:
        return book, f'\n<<< This phone number not found!\n'
