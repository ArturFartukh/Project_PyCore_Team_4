from Support_funcs.split_data import *


def add_note_func(data: str, book):
    name, note = split_data(data)
    if name not in book.data.keys():
        return book, '\nThis user not in contact book.\n'
    record = book[name]
    if not note:
        note = input('Please enter note: ')
    record.add_note(note)
    return book, f'\nNote has been added to contact: [{name}]\n'


def search_in_notes_func(data: str, book) -> str:
    name, search = split_data(data)
    if name not in book.data.keys():
        return '\nThis user not in contact book.\n'
    record = book[name]
    if not record.notes:
        return f'\n{name} don`t have notes\n'
    else:
        output_message = ''
        index = 0
        for note in record.notes:
            index += 1
            if note.value.lower().find(search.lower()) >= 0:
                output_message += f'{index}. {note.value}\n'
        if not output_message:
            return '\nCould n`t find anything\n'
        else:
            return output_message


def change_notes_func(data: str, book):
    name, note = split_data(data)
    if name not in book.data.keys():
        return f'This user not in contact books'
    record = book[name]
    if note:
        note = input('Please enter note: ')
        record.add_note(note)
    return f'User: {name} note has been changed '
