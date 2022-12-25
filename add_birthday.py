def add_birthday(data: str):
    name, birth_date = split_data(data)
    if name in book.data.keys():
        contact = book.data[name]
        contact.birthday = contact.add_birthday(birth_date)
        return f'\nBirthday has been added [{name}]:[{contact.birthday}]\n'
    else:
        raise ValueError('This user not in contact book')