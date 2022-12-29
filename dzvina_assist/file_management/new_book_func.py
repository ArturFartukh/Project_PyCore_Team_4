from dzvina_assist.Classes import AddressBook
from dzvina_assist.file_management import save_func


def new_book_func(save, book):
    if book.book_name:
        choice = input('Do you want save changes in this book? y/n: ')
        if choice.lower() in ('y', 'yes'):
            save_func(save, book)
    print('For exit enter: exit')
    while True:
        new_book_name = input('Enter the name of the new book: ')
        if new_book_name.lower() == 'exit':
            return '<<< \033[33mCancellation of book creation...\033[0m\n'
        if new_book_name and new_book_name not in save.data:
            book = AddressBook()
            book.change_book_name(new_book_name)
            return book
        print('\033[33mA book with that name already exists.\033[0m')
        print('Try again.')
