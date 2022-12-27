from support_funcs import split_data


def add_address_func(data: str, book):
    name, address = split_data(data)
    if name not in book.data:
        return book, '\nThis user not in contact book.\n'
    contact = book[name]
    if contact.address:
        return book, '\nThis contact already exist address.\n'
    if not address:
        address = input('Please enter an address: ')
    if contact.add_address(address):
        return book, f'\nAddress: [{address}] has been added to contact [{name}].\n'
    return print('\nThis is really address?\n\033[31mCanceling address saving...\033[0m\n')


def change_address_func(data: str, book):
    name, address = split_data(data)
    if name not in book.data:
        return book, '\nThis user not in contact book.\n'
    contact = book[name]
    if not address:
        address = input('Please enter new address: ')
    contact.add_address(address)
    return book, f'\nAddress: [{address}] has been changed to contact [{name}]/\n'
