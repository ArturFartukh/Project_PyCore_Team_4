from split_data import *


def del_func(data: str, book):
    """Deleting contact to the address book"""
    name, phone = split_data(data)
    if name not in book.data.keys():
        return book, f'\nContact with name [{name}] not found!\n'
    contact = book.data[name]
    if contact.phone_in_contact(phone):
        confirmation = input(f'Do you want to delete phone [{phone}]? Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            contact.del_phone(phone)
            return book, f'\nNumber [{phone}] has been deleted from [{name}]\n'
        else:
            return book, '\nContinue\n'
    elif not phone:
        confirmation = input(f'Do you want to delete contact [{name}] completely? Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            book.del_record(name)
            return book, f'\nContact [{name}] has been deleted!!!\n'
        else:
            return book, '\nContinue\n'
    else:
        return book, f'\nThis phone number not found!\n'
        