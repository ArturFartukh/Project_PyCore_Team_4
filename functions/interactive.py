from Classes import AddressBook
from file_management import sorting_files, new, save, load
from functions import *

book = AddressBook()


def start():
    """Main function"""
    print('Start!\n')
    print('To see the available commands, enter "info" bks of quotes.')
    while True:
        input_command = input('>>> ')
        if input_command.lower() in STOP_LIST:
            if input('Do you want to save the book? Y/N: ').upper() in ('Y', 'YES'):
                save_book()
            print('Good bye!')
            break

        result = command_parser(input_command)
        print(result)


def command_parser(input_command: str):
    """Processing the command entered by the user"""

    new_input = input_command.split()
    new_input = [item.lower().strip() for item in new_input if item not in ('', ' ')]
    input_command = ' '.join(new_input)
    data = ''
    command = ''
    for key in OPERATIONS:
        if input_command.startswith(key):
            command = key
            data = input_command[len(command):]
            data = data.strip()
            break
    if data:
        return func_call(command)(data)
    return func_call(command)()


def func_call(command: str):
    """Calling a function depending on the entered command"""

    return OPERATIONS.get(command, unknown_command)


def unknown_command():
    return 'Wrong input!'


def info_funk() -> str:
    return '\nMain commands:\n' \
           'new book - create a new book\n' \
           'load book - load the book\n' \
           'save book - save the book\n' \
           'organize files - [organize files Path] - Sorts the files in the specified directory\n' \
           'add contact - [add Name 0123456789] - add new contact/contact and number\n' \
           'change phone - [change phone Name] - change contact number\n' \
           'del contact - [del Name 0123456789] - delete contact/contact number\n' \
           'add address - [add address Name Address] - add address to a contact\n' \
           'change address - [change address Name] - change contact address\n' \
           'add email - [add email Name E-mail] - add e-mail to a contact\n' \
           'change email - [change email Name E-mail] - change e-mail in contact\n' \
           'add birthday - [add birthday dd.mm.yyyy] - add birthday to а contact\n' \
           'when birthday - [when birthday Name] - remaining days until the birthday\n' \
           'add note - [add note Note] - add note to а contact\n' \
           'find note - [find note Name string] - find note in contact\n' \
           'add tags - [add tags Name] - add tags to а contact\n' \
           'tag - [tag Str] - find to tag\n' \
           'find tag - [find tag Tag] - searches for a note by tag\n' \
           'find - [find Name/Number] - search for a contact by name/number\n' \
           'gfind - [gfind Name/Number] - find a contact by name/number in all saved books\n' \
           'about contact - [about contact Name] - all contact information\n' \
           'about all - all information about all contacts\n' \
           'all phones - show all numbers in the book\n'


def hello_func():
    return '\nHello! How can I help you?\n'


def new_book():
    global book
    book, result = new()
    return result


def load_book():
    global book
    book, result = load(book)
    return result


def save_book():
    global book
    book, result = save(book)
    return result


def organize_files(path=''):
    if not path:
        path = input('Enter the directory path: ')
    return sorting_files(path)


def add_contact(data: str) -> str:
    global book
    book, result = add_func(data, book)
    return result


def change_phone(data: str) -> str:
    global book
    book, result = change_phone_func(data, book)
    return result


def del_contact_or_number(data: str) -> str:
    global book
    book, result = del_func(data, book)
    return result


def add_address(data: str) -> str:
    global book
    book, result = add_address_func(data, book)
    return result


def change_address(data: str) -> str:
    global book
    book, result = change_address_func(data, book)
    return result


def add_email(data: str) -> str:
    global book
    book, result = add_email_func(data, book)
    return result


def change_email(data: str) -> str:
    global book
    book, result = change_email_func(data, book)
    return result


def add_birthday(data: str) -> str:
    global book
    book, result = add_birthday_func(data, book)
    return result


def when_birthday(data: str) -> str:
    global book
    result = days_before_birthday_func(data, book)
    return result


def add_note(data: str) -> str:
    global book
    book, result = add_note_func(data, book)
    return result


def change_note(data: str) -> str:
    global book
    book, result = change_notes_func(data, book)
    return result


def del_note(data: str) -> str:
    global book
    book, result = del_note_func(data, book)
    return result


def search_in_notes(data: str) -> str:
    global book
    result = search_in_notes_func(data, book)
    return result


def add_tags(data: str) -> str:
    global book
    book, result = add_tags_func(data, book)
    return result


def search_to_teg(data: str) -> str:
    global book
    result = find_tags_func(data, book)
    return result


def search_contact(data: str) -> str:
    global book
    result = search_contact_func(data, book)
    return result


def global_search(data: str) -> str:
    global book
    result = search_contact_global_func(data)
    return result


def contact_info(name: str) -> str:
    global book
    result = contact_info_func(name, book)
    return result


def all_contact_info() -> str:
    global book
    result = all_contact_info_func(book)
    return result


def all_numbers() -> str:
    global book
    result = all_numbers_func(book)
    return result


OPERATIONS = {'info': info_funk,
              'new book': new_book,
              'load book': load_book,
              'save book': save_book,
              'organize files': organize_files,
              'hello': hello_func,
              'hi': hello_func,
              'add contact': add_contact,
              'change phone': change_phone,
              'del contact': del_contact_or_number,
              'add address': add_address,
              'change address': change_address,
              'add email': add_email,
              'change email': change_email,
              'add birthday': add_birthday,
              'when birthday': when_birthday,
              'add note': add_note,
              'change note': change_note,
              'del note': del_note,
              'find note': search_in_notes,
              'add tags': add_tags,
              'tag': search_to_teg,  # !!!
              'find': search_contact,
              'gfind': global_search,
              'about contact': contact_info,
              'about all': all_contact_info,
              'all phones': all_numbers
              }

STOP_LIST = ('good bye',
             'close',
             'exit',
             'bye',
             'end',
             'stop',
             'break',
             '.'
             )
