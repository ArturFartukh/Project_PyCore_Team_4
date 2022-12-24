from datetime import datetime

def add_birthday(data: str) -> str:
    name, birth_date = split_data(data)
    if name in book.data.keys():
        contact = book.data[name]
        birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        contact.birthday = birth_date
        return f'\nBirthday has been added [{name}]:[{contact.birthday}]\n'
    else:
        raise ValueError('This user not in contact book')