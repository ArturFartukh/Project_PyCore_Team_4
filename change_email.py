from split_data import split_data


def change_email(data: str) -> str:
    name, email_new = split_data(data)
    if name not in book.data.keys():
        raise ValueError('This user not in contact book')
    record = book[name]
    if not record.email:
        record.add_email(email_new)
        return f'Email: {email_new} has been added to contact: {name}'
    else:
        user_command = input(f'{name} already has an email. Do you want change {record.email} to {email_new}?:\n').strip().lower()
        if user_command == 'yes' or user_command == 'y':
            record.add_email(email_new)
            return f'\nThe contact email has been changed to {email_new}\n'
        else:
            return f'Email has not been changed'
