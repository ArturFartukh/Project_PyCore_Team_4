from BookClasses import Record
from Support_funcs.split_data import *
from Support_funcs.phone_validator import *


def add_func(data: str, book):
    """Adding contact to the address book"""
    
    name, phone = split_data(data)

    if name not in book.data.keys() and not phone:
        new_contact = Record(name)
        book.add_record(new_contact)
        return book, f'\nNew contact has been added:\n[{name}]\n'
    elif name not in book.data.keys() and phone:
        new_contact = Record(name, phone)
        book.add_record(new_contact)
        return book, f'\nNew contact has been added:\n[{name}]:[{phone}]\n'
    
    contact = book.data[name]
    if contact.phone_in_contact(phone):
        return book, f'This phone number already exists!'
    elif not contact.phone_in_contact(phone) and phone:
        contact.add_phone(phone)
        return book, f'\nNumber [{phone}] has been added to contact: [{name}]\n'
    else:
        return book, '\nThis contact already exists!\n'


def change_phone_func(data: str, book):
    """Changing an existing contact number"""
    name, phone_old = split_data(data)

    if name in book.data.keys():
        contact = book.data[name]
        if contact.phone_in_contact(phone_old):
            phone_new = input('Please enter new phone number: ')
            phone_new = phone_validator(phone_new)
            contact.change_phone(phone_old, phone_new)
            return book, f'\nThe contact number has been changed from:\n[{phone_old}] to [{phone_new}]\n'
        else:
            return book, f"\nThis phone number doesn't exist!"
    else:
        return book, "This contact doesn't exist!"


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
