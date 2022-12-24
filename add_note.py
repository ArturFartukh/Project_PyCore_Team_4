from split_data import split_data


def add_note(data: str) -> str:
    name, note = split_data(data)
    if name not in book.data.keys():
        raise ValueError('This user not in contact book')
    record = book[name]
    record.add_note(note)
    return f'\nNote has been added to contact: [{name}]\n'
