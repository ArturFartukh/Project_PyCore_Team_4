from Project_PyCore_Team_4 import Record, AddressBook


def add_email(data: str):
    name, email = split_data(data)
    if name not in book:
        raise ValueError('This user not in contact book')
    record = Record(name)
    for mail in email:
        raise ValueError('Email for this contact already exist')
    record = add_email(mail)

    return f'Email: {email} has been added to contact: {name}'


