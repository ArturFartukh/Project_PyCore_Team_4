from Project_PyCore_Team_4 import Record, AddressBook


def add_email(data: str):
    name, email = split_data(data)
    if book.name:
        raise ValueError('This user not in contact book')
    if book.mail:
        raise ValueError('Email for this contact already exist')
    record = add_email(email)
    book.add_record(record)
    return f'Email: {email} has been added to contact: {name}'


