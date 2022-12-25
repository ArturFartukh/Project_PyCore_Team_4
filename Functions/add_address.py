from main import book
from split_data import *


def add_address(data: str):
    name, address = split_data(data)
    if name not in book.data.keys():
        raise ValueError('This user not in contact book')
    if book.address:
        raise ValueError('This contact already exist address')
    record = book[name]
    if not address:
        address = input('Please enter an address: ')
    record.add_address(address)
    return f'Address: {address} has been added to contact {name}'
