from main import book
from split_data import split_data


def search_in_notes(data: str) -> str:
    name, search = split_data(data)
    if name not in book.data.keys():
        raise ValueError('This user not in contact book')
    record = book[name]
    if not record.notes:
        return f'{name} don`t have notes'
    else:
        output_message = ''
        index = 0
        for note in record.notes:
            index += 1
            if note.value.lower().find(search.lower()) >= 0:
                output_message += f'{index}. {note.value}\n'
        if not output_message:
            return 'Couldn`t find anything'
        else:
            return output_message
        