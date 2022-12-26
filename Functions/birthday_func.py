from support_funcs import split_data


def add_birthday_func(data: str, book):
    name, birth_date = split_data(data)
    if name in book.data.keys():
        contact = book.data[name]
        contact.add_birthday(birth_date)
        return book, f'\nBirthday has been added [{name}]:[{contact.birthday}]\n'
    else:
        return book, 'This user not in contact book'


def days_before_birthday_func(data: str, book):
    name = data.strip().title()
    if name not in book:
        raise ValueError('No such contact found!')
    record = book[name]
    result = record.next_birthday()
    return result
