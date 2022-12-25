from main import book
from split_data import *


def change_email(data: str) -> str:
    name, email_new = split_data(data)
    if name not in book.data.keys():
        raise ValueError('This user not in contact book')
    record = book[name]
    if not record.email:
        record.add_email(email_new)
        return f'Email: {email_new} has been added to contact: {name}'
    else:
        user_command = input(f'{name} already has an email.\n'
                             f'Do you want change {record.email} to {email_new}?: Y/N').strip().lower()
        if user_command in ('yes', 'y'):
            record.add_email(email_new)
            return f'\nThe contact email has been changed to {email_new}\n'
        else:
            return f'Email has not been changed'
