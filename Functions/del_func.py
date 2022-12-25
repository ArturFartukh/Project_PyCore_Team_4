from main import book
from split_data import *


def del_func(data: str):
    """Deleting contact to the address book"""
    name, phone = split_data(data)
    if name not in book.data.keys():
        return f'\nContact with name {name} not found!\n'
    contact = book.data[name]
    if contact.phone_in_contact(phone):
        confirmation = input(f'Do you want to delete phone {name}? Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            contact.del_phone(phone)
            return f'\nNumber [{phone}] has been deleted from [{name}]\n'
        else:
            return '\nContinue\n'
    elif not phone:
        confirmation = input(f'Do you want to delete contact {name} completely? Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            book.del_record(name)
            return f'\nContact [{name}] has been deleted!!!\n'
        else:
            return 
    else:
        return f'\nThis phone number not found!\n'
        