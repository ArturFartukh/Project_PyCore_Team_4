from BookClasses import AddressBook
from work_with_files import new, save, load
from Functions.add_func import *
from Functions.change_phone import *
from Functions.del_func import *
# from Functions.add_address import *
# from Functions.add_email import *
# from Functions.change_email import *
# from Functions.add_birthday import *
# from Functions.when_birthday import *
# from Functions.add_note import *
# from Functions.searsh_contact import *
from Functions.all_numbers_func import *


def main():
    """Main function"""
    
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
           'add - "add Name 0123456789" - add new contact/contact and number\n'\
           'change phone - "change phone  Name 0123456789" - change contact number\n'\
           'del - "del Name 0123456789" - delete contact/contact number\n'\
           'add address - "add address Name Address" - add address to a contact\n'\
           'add email - "add email Name E-mail" - add e-mail to a contact\n'\
           'change email - "change email Name E-mail" - change e-mail in contact\n'\
           'add birthday - "add birthday dd.mm.yyyy" - add birthday to а contact\n'\
           'when birthday - "when birthday Name" - remaining days until the birthday\n'\
           'add note - add note Note - add note to а contact\n'\
           'find note - find note string - find note in contact\n'\
           'add tags - add tags Tag1 Tag2 ... - add tags to а contact\n'\
           'find tag - find tag Tag - searches for a note by tag\n'\
           'find - find Name/Number - search for a contact by name/number\n'\
           'gfind - gfind Name/Number - find a contact by name/number in all saved books\n'\
           'about - about Name - all contact information\n'\
           'about all - all information about all contacts\n'\
           'all numbers - show all numbers in the book\n'


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


def all_numbers() -> str:
    global book
    result = all_numbers_func(book)
    return result


OPERATIONS = {'info': info_funk,
              'new book': new_book,
              'load book': load_book,
              'save book': save_book,
              'hello': hello_func,
              'hi': hello_func,
              'add': add_contact,
              'change phone': change_phone,
              'del': del_contact_or_number,
              #'add address': add_address,
              #'add email': add_email,
              #'change email': change_email,
              #'add birthday': add_birthday,
              #'when birthday': days_before_birthday,
              #'add note': add_note,
              #'find note': search_in_notes,
              #'find': searsh_contact,
              #'gfind': global_search,
              #'about': about,
              #'about all': about_all,
              'all numbers': all_numbers
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

if __name__ == '__main__':

    book = AddressBook()

    main()
