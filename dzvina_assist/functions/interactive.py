from dzvina_assist.Classes import Save
from dzvina_assist.Classes import AddressBook
from dzvina_assist.support_funcs import input_error
from dzvina_assist.file_management import sorting_files, new_book_func, save_func, load_func
from dzvina_assist.functions import *
from fuzzywuzzy import process
import pickle

book = AddressBook()

try:
    with open(f'save.dat', 'rb') as fh:
        save = pickle.load(fh)
except FileNotFoundError:
    with open(f'save.dat', 'wb') as fh:
        save = Save()
        pickle.dump(save, fh)


def start():
    """Main function"""
    print('Start!')
    print('~' * 57)
    print('To see the available commands, enter "\033[32m\033[1minfo\033[0m" bks of quotes.\n')
    while True:
        print('1 New book\n'
              '2 Load book\n'
              '3 Save book\n'
              '4 All commands')
        print('Make a choice or enter a command.')
        input_command = input('>>> ')
        if input_command.lower() in STOP_LIST:
            if input('\033[32mDo you want to save the book? Y/N: \033[0m').upper() in ('Y', 'YES'):
                save_book()
            with open(f'save.dat', 'wb') as file:
                pickle.dump(save, file)
            print('\033[32mGood bye!\033[0m')
            break

        result = command_parser(input_command)
        print(result)


# @input_error
def command_parser(input_command: str):
    """Processing the command entered by the user"""

    new_input = input_command.split()
    new_input = [item.lower().strip() for item in new_input if item not in ('', ' ')]
    input_command = ' '.join(new_input)
    command_fuzz = list(process.extractOne(input_command, OPERATIONS.keys()))
    command = command_fuzz[0]
    data = input_command[len(command):].strip()
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
           'new_book book - create a new_book book\n' \
           'load book - load the book\n' \
           'save book - save the book\n' \
           'organize files - [organize files Path] - Sorts the files in the specified directory\n' \
           'add contact - [add Name 0123456789] - add new_book contact/contact and number\n' \
           'change phone - [change phone Name] - change contact number\n' \
           'del contact - [del Name 0123456789] - delete contact/contact number\n' \
           'add address - [add address Name Address] - add address to a contact\n' \
           'change address - [change address Name] - change contact address\n' \
           'add email - [add email Name E-mail] - add e-mail to a contact\n' \
           'change email - [change email Name E-mail] - change e-mail in contact\n' \
           'add birthday - [add birthday Name dd.mm.yyyy] - add birthday to а contact\n' \
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
    return '\nHello! My name is Dzvina.\nHow can I help you?\n'


def new_book():
    global book
    result = new_book_func()
    if isinstance(result, str):
        return result
    book = result
    return f'<<< \033[32mA new_book book [\033[1m{book.book_name}\033[0m\033[32m] has been created.\033[0m'


def load_book():
    # global save
    global book
    result = load_func(save)
    if isinstance(result, str):
        return result
    book = result
    return f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m] has been loaded.\033[0m\n'


def save_book():
    global save
    global book
    save, book, result = save_func(save, book)
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
              '1': new_book,
              '2': load_book,
              '3': save_book,
              '4': info_funk,
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
