from main import book
import phone_validator
from split_data import *


def change_phone_func(data: str):
    """Changing an existing contact number"""
    name, phone_old = split_data(data)

    if name in book.data.keys():
        contact = book.data[name]
        if contact.phone_in_contact(phone_old):
            phone_new = input('Please enter new phone number: ')
            phone_new = phone_validator(phone_new)
            contact.change_phone(phone_old, phone_new)
            return f'\nThe contact number has been changed from:\n[{phone_old}] to [{phone_new}]\n'
        else:
            return f"\nThis phone number doesn't exist!"
    else:
        "This contact doesn't exist!"
