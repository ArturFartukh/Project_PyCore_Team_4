from main import book
from split_data import *
from BookClasses import Record


def add_func(data: str):
    """Adding contact to the address book"""
    
    name, phone = split_data(data)

    if name not in book.data.keys() and not phone:
        new_contact = Record(name)
        book.add_record(new_contact)
        return f'\nNew contact has been added:\n[{name}]\n'
    elif name not in book.data.keys() and phone:
        new_contact = Record(name, phone)
        book.add_record(new_contact)
        return f'\nNew contact has been added:\n[{name}]:[{phone}]\n'
    
    contact = book.data[name]
    if contact.phone_in_contact(phone):
        return f'This phone number already exists!'
    elif not contact.phone_in_contact(phone) and phone:
        contact.add_phone(phone)
        return f'\nNumber [{phone}] has been added to contact: [{name}]\n'
    else:
        return '\nThis contact already exists!\n'
