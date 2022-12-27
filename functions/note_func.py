from support_funcs import split_data


def add_note_func(data: str, book):
    name, note = split_data(data)
    if name not in book.data.keys():
        return book, '\n<<< This user not in contact book.\n'
    record = book[name]
    if not note:
        note = input('Please enter note: ')
    record.add_note(note)
    return book, f'\n<<< Note has been added to contact: [{name}]\n'


def change_notes_func(name: str, book):
    name = name.strip().title()
    if name not in book.data.keys():
        return book, f'\nContact with name [{name}] not found!\n'
    record = book[name]
    if not record.notes:
        return book, f'\nContact [{name}] has no notes.\n'
    for count, note in enumerate(record.notes, 1):
        print(f'{count} {note}')
    choice = input('Select a number to change: ')
    if int(choice) > len(record.notes):
        return book, '\nWrong choice.'
    note = input('Write a note: ')
    record.change_note(choice, note)
    return book, f'User: {name} note has been changed '


def del_note_func(name: str, book):
    name = name.strip().title()
    if name not in book.data.keys():
        return book, f'\nContact with name [{name}] not found!\n'
    record = book[name]
    if not record.notes:
        return book, f'\nContact [{name}] has no notes.\n'
    for count, note in enumerate(record.notes, 1):
        print(f'{count} {note}\n')
    choice = input('Select a number to change: ')
    if int(choice) > len(record.notes):
        return book, '\nWrong choice.'
    confirmation = input(f'Are you sure you want to delete the note? Y/N: ')
    if confirmation.lower() in ('y', 'yes'):
        record.del_note(choice)
        return book, f'\nNote has been deleted.\n'
    else:
        return book, '\nAbolition...\n'


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
