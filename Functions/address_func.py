from split_data import *


def add_address_func(data: str, book):
    name, address = split_data(data)
    if name not in book.data.keys():
        return book, '\nThis user not in contact book.\n'
    contact = book[name]
    if contact.address:
        return book, '\nThis contact already exist address.\n'
    if not address:
        address = input('Please enter an address: ')
    contact.add_address(address)
    return book, f'\nAddress: [{address}] has been added to contact [{name}].\n'


def change_address_func(data: str, book):
    name, address = split_data(data)
    if name not in book.data.keys():
        return book, '\nThis user not in contact book.\n'
    contact = book[name]
    if not address:
        address = input('Please enter new address: ')
    contact.add_address(address)
    return book, f'\nAddress: [{address}] has been changed to contact [{name}]/\n'