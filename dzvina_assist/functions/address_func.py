def add_address_func(book):

    name = input('Please enter name: ')
    name = name.strip().title()
    if name not in book.data:
        return book, '\n<<< This user not in contact book.\n'
    address = input('Please enter an address: ')
    address = address.strip()
    contact = book[name]
    if contact.address:
        return book, '\n<<< This contact already exist address.\n'
    if contact.add_address(address):
        return book, f'\nA<<< Address: [{address}] has been added to contact [{name}].\n'
    return '\n<<< This is really address?\n\033[31mCanceling address saving...\033[0m\n'


def change_address_func(book):

    name = input('Please enter name: ')
    name = name.strip().title()
    if name not in book.data:
        return book, '\n<<< This user not in contact book.\n'
    contact = book[name]
    address = input('Please enter new address: ')
    address = address.strip()
    contact.add_address(address)
    return book, f'\n<<< Address: [{address}] has been changed to contact [{name}]/\n'
