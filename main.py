from BookClasses import AddressBook
from work_with_files import new_book, save_book, load_book
from Functions.hello_func import *
from Functions.add_func import *
from Functions.change_phone import *
from Functions.del_func import *
from Functions.add_address import *
from Functions.add_email import *
from Functions.change_email import *
from Functions.add_birthday import *
from Functions.when_birthday import *
from Functions.add_note import *
from Functions.searsh_contact import *


def main():
    """Main function"""
    
    while True:
        input_command = input('>>> ')
        if input_command.lower() in STOP_LIST:
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


OPERATIONS = {'info': info_funk,
              'new book': new_book,
              'load book': load_book,
              'save book': save_book,
              'hello': hello_func,
              'hi': hello_func,
              'add': add_func,
              'change phone': change_phone_func,
              'del': del_func,
              'add address': add_address,
              'add email': add_email,
              'change email': change_email,
              'add birthday': add_birthday,
              'when birthday': days_before_birthday,
              'add note': add_note,
              'find': searsh_contact,
              'glob find': global_search,
              'show all': show_all
              }


STOP_LIST = ('good bye', 'close', 'exit', '.')


if __name__ == '__main__':

    book = AddressBook()

    main()
