from main import *
from split_data import *


def add_email(data: str):
    name, email = split_data(data)
    if name not in book.data.keys():
        raise ValueError('This user not in contact book')
    if book.email:
        raise ValueError('Email for this contact already exist')
    record = book[name]
    record.add_email(email)
    return f'Email: {email} has been added to contact: {name}'
