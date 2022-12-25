from main import book
from BookClasses import AddressBook
import pickle


def new_book() -> str:
    book_name = input('Enter new book name: ')
    book_name = book_name.strip()
    book = AddressBook()
    book.change_book_name(book_name)
    return f'A new book [{book_name}] has been created.\n'


def save_book() -> str:

    if not book.book_name:
        print('This is a new book.\n')
        new_book_name = input('Please enter new book name: ')
        book.change_book_name(new_book_name)

    with open('saved_books.txt', 'r') as file_r:
        books_list = file_r.readlines()
        if f'{book.book_name}\n' not in books_list:
            with open('saved_books.txt', 'a') as file_a:
                file_a.write(f'{book.book_name}\n')
            with open(book.book_name + '.dat', 'wb') as fh:
                pickle.dump(book, fh)
            return f'The book [{book.book_name}] was saved.\n'
        else:
            print(f'A book with the name {book.book_name} already exists.\n')
            print('What action do you want to perform?:\n'
                  '1 Enter another name\n'
                  '2 Combine both books and save\n'
                  '3 Replace the saved book with a new one\n'
                  '4 Cancel save\n')
            user_choice = input('Enter your choice: ')
            if user_choice == '1':
                while True:
                    print('For exit enter: exit\n')
                    new_book_name = input('Enter new name: ')
                    if new_book_name.lower() == 'exit':
                        return 'Cancel saving the book...\n'
                    if f'{book.book_name}\n' not in books_list:
                        book.change_book_name(new_book_name)
                        with open('saved_books.txt', 'a') as file_a:
                            file_a.write(f'{book.book_name}\n')
                        with open(book.book_name + '.dat', 'wb') as fh:
                            pickle.dump(book, fh)
                        return f'The book [{book.book_name}] was saved.\n'
                    print(f'A book with the name {book.book_name} already exists.\n')
                    print('Try again.\n')
            elif user_choice == '2':
                try:
                    with open(book.book_name + '.dat', 'rb') as fh:
                        old_book = pickle.load(fh)
                        book.merging_books(old_book)
                except FileNotFoundError:
                    raise FileNotFoundError('File not found.\n')
                with open(book.book_name + '.dat', 'wb') as fh:
                    pickle.dump(book, fh)
                return 'The books were merged and saved.\n'
            elif user_choice == '3':
                try:
                    with open(book.book_name + '.dat', 'wb') as fh:
                        pickle.dump(book, fh)
                    return f'The book [{book.book_name}] was rewritten.\n'
                except FileNotFoundError:
                    raise FileNotFoundError('File not found.\n')
            elif user_choice == '4':
                return 'Cancel save...\n'
            else:
                return 'Unknown command!\nAbort save...'


def load_book() -> str:
    try:
        with open('saved_books.txt', 'r') as fh:
            book_list = fh.readlines()
            print('\nSaved books:')
            for book_name in book_list:
                print(book_name, end='')
    except FileNotFoundError:
        print('\nSaved books not found.\n')
        user_choice = input('Do you want to create a new book? Y/N: ')
        if user_choice.upper() == 'Y':
            return new_book()
        elif user_choice.upper() == 'N':
            return '\nCancel load...\n'
        else:
            return 'Unknown command\nAbort...'

    book_file = input('\nEnter book name: ')
    try:
        with open(book_file + '.dat', 'rb') as fh:
            book = pickle.load(fh)
            return f'\nThe book [{book.book_name}] has been loaded.\n'
    except FileNotFoundError:
        return '\nFile not found...\nAbort loading...\n'
