from BookClasses import Record
from Support_funcs.split_data import split_data


def del_note(data: str, book):
    name, note = split_data(data)
    if name not in book.data.keys():
        return book, f'\nContact with name [{name}] not found!\n'
    record = book.data[name]
    if record.search_in_notes_func(note):
        confirmation = input(f'Do you want to delete note [{note}]? Y/N: ')
        if confirmation.lower() in ('y', 'yes'):
            record.del_note(note)
            return book, f'\nNote [{note}] has been deleted from\n'
        else:
            return book, '\nContinue\n'
