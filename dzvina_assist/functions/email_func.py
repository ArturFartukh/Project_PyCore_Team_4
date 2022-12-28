from dzvina_assist.support_funcs import split_data


def add_email_func(data: str, book):
    name, email = split_data(data)
    if name not in book.data:
        return book, '\n<<< This user not in contact book.\n'
    contact = book[name]
    if contact.email:
        return book, '\n<<< Email for this contact already exist\n'
    if not email:
        email = input('Please enter email address: ')
    contact.add_email(email)
    return book, f'\n<<< Email: [{email}] has been added to contact: [{name}]\n'


def change_email_func(data: str, book):
    name, email = split_data(data)
    if name not in book.data:
        return book, '\n<<< This user not in contact book.\n'
    contact = book[name]
    if not email:
        email = input('Please enter new email: ')
    contact.add_email(email)
    return book, f'\n<<< Email: [{email}] has been changed to contact [{name}]\n'
