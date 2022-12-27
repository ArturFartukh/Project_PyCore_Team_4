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
        return book, '\n<<< This contact exists./\033[31mInvalid phone!\033[0m\n'


def change_phone_func(data: str, book):
    """Changing an existing contact number"""
    name = data.strip().title()

    if name not in book.data.keys():
        return book, "<<< This contact doesn't exist!"

    contact = book.data[name]

    all_phones = contact.get_all_phones()
    for count, number in enumerate(all_phones, 1):
        print(f'{count} {number}')
    choice = input('Select a number to replace: ')
    if not choice.isdigit() or not 0 < int(choice) <= len(all_phones):
        return book, '\033[31mWrong choice.\nAbolition...\033[0m\n'
    new_phone = input('Enter a new number: ')
    new_phone = phone_validator(new_phone)
    if not new_phone:
        return book, '\033[31mInvalid number format.\nAbolition...\033[0m\n'
    contact.change_phone(choice, new_phone)
    return book, f'\n<<< The contact number has been changed to [{new_phone}]\n'


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
