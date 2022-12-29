from dzvina_assist.Classes import Record
from dzvina_assist.support_funcs import phone_validator


def add_func(book):
    """Adding contact to the address book"""

    name = input('Please enter [name]: ')
    name = name.strip().title()

    choice = input('Do you want add phone? y/n: ')
    if choice.lower() in ('y', 'yes'):
        phone = input('Enter phone number: ')
        phone = phone_validator(phone)
    elif choice.lower() in ('n', 'no'):
        phone = ''
    else:
        return book, '\n<<< \033[33mInvalid choice!\033[0m\n'

    if name not in book.data and not phone:
        new_contact = Record(name)
        book.add_record(new_contact)
        print('\n<<< \033[31m!!! The phone number is not specified.\n!!! Or is specified in the wrong format.\033[0m')
        return book, f'\n<<< New contact has been added:\n[{name}]:[\033[31m\033[1m\033[4mNo number available\033[0m]\n'
    elif name not in book.data and phone:
        new_contact = Record(name, phone)
        book.add_record(new_contact)
        return book, f'\n<<< New contact has been added:\n[{name}]:[{phone}]\n'

    contact = book.data[name]
    if contact.has_phone(phone):
        return book, f'<<< This phone number already exists!'
    elif phone:
        contact.add_phone(phone)
        return book, f'\n<<< Number [{phone}] has been added to contact: [{name}]\n'
    else:
        return book, '\n<<< This contact exists./\033[31mInvalid phone!\033[0m\n'


def change_phone_func(book):
    """Changing an existing contact number"""

    name = input('Please enter name: ')
    name = name.strip().title()
    if name not in book.data:
        return book, "<<< This contact doesn't exist!"

    contact = book.data[name]

    all_phones = contact.get_all_phones()
    for count, number in enumerate(all_phones, 1):
        print(f'{count} {number}')
    choice = input('Select a number to replace: ')
    choice = choice.strip()
    if not choice.isdigit() or not 0 < int(choice) <= len(all_phones):
        return book, '<<< \033[31mWrong choice.\nAbolition...\033[0m\n'
    new_phone = input('Enter a new number: ')
    new_phone = phone_validator(new_phone)
    if not new_phone:
        return book, '<<< \033[31mInvalid number format.\nAbolition...\033[0m\n'
    contact.change_phone(choice, new_phone)
    return book, f'\n<<< The contact number has been changed to [{new_phone}]\n'


def del_func(book):
    """Deleting contact to the address book"""
    if not book.data:
        return book, 'This book has no contacts.\n'
    name = input('Please enter name: ')
    name = name.strip().title()
    if name not in book.data:
        return book, f'\n<<< Contact with name [{name}] not found!\n'
    contact = book.data[name]
    print('1 Del all contact\n2 Del number from contact')
    choice = input('Make your choice: ')
    choice = choice.strip()
    if choice == '1':
        confirmation = input(f'\033[33mAre you sure??\033[0m Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            book.del_record(name)
            return book, f'\n<<< Contact [{name}] has been deleted!!!\n'
        else:
            return book, '\n<<< Abolition...\n'
    elif choice == '2':
        if not book.phones:
            return book, '\033[33mThis contact has no numbers.\033[0m'
        for count, phone in enumerate(book.phones, 1):
            print(f'{count} {phone}')
        choice = input('Make your choice: ')
        choice = choice.strip()
        contact.del_phone(choice)
        return book, f'\n<<< Number has been deleted from [{name}]\n'
    else:
        return book, f'\n<<< Wrong choice!\n'
