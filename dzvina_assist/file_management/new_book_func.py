from dzvina_assist.Classes import AddressBook


def new_book_func():
    print('For exit enter: exit')
    while True:
        new_book_name = input('Enter the name of the new book: ')
        if new_book_name.lower() == 'exit':
            return '<<< \033[33mCancellation of book creation...\033[0m\n'
        if new_book_name:
            book = AddressBook()
            book.change_book_name(new_book_name)
            return book
        print('Try again.')
