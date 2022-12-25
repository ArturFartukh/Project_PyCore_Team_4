from BookClasses import AddressBook


def main():
    '''Main function'''
    
    while True:
        input_command = input('>>> ')
        if input_command.lower() in STOP_LIST:
            print('Good bye!')
            break

        result = command_parser(input_command)
        print(result)


def command_parser(input_command: str):
    '''Processing the command entered by the user'''
    
    new_input = input_command.split()
    new_input = [item.lower() for item in new_input if item not in ('', ' ')]
    input_command = ' '.join(new_input)
    data = ''
    for key in OPERATIONS:
        if input_command.startswith(key):
            command = key
            data = input_command[len(new_input):]
            break
        if data:
            return func_call(command)(data)
        return func_call(command)()


def func_call(command: str):
    '''Calling a function dependштп on the entered command'''
    
    return OPERATIONS.get(command, unknown_command)


def unknown_command():
    return 'Wrong input!'


OPERATIONS = {}


STOP_LIST = ('good bye', 'close', 'exit', '.')


if __name__ == '__main__':

    book = AddressBook()

    main()