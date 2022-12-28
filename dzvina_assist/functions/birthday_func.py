from support_funcs import split_data


def add_birthday_func(data: str, book):

    name, birth_date = split_data(data)

    if name not in book.data:
        return book, '<<< This user not in contact book'

    contact = book.data[name]
    data = ''
    for i in birth_date:
        if i.isdigit():
            data += i
        else:
            data += '.'
    birth_date = data

    if birth_date[0: 3].isdigit():
        birth_date = birth_date.split('.')
        birth_date = birth_date[::-1]
        birth_date = '.'.join(birth_date)

    contact.add_birthday(birth_date)

    return book, f'\n<<< Birthday has been added [{name}]:[{contact.birthday}]\n'


def days_before_birthday_func(data: str, book):

    name = data.strip().title()

    if name not in book:
        return '<<< No such contact found!'

    record = book[name]
    result = record.next_birthday()

    return result
