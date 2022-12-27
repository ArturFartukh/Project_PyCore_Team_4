from BookClasses import AddressBook
import pickle


def new():
    book_name = input('Enter new book name: ')
    book_name = book_name.strip()
    book = AddressBook()
    book.change_book_name(book_name)
    return book, f'A new book [{book_name}] has been created.\n'


def save(book):

    if not book.book_name:
        print('This is a new book.\n')
        new_book_name = input('Please enter new book name: ')
        book.change_book_name(new_book_name)

    with open('../saved_books/saved_books.txt', 'r') as file_r:
        books_list = file_r.readlines()
        if f'{book.book_name}\n' not in books_list:
            with open('../saved_books/saved_books.txt', 'a') as file_a:
                file_a.write(f'{book.book_name}\n')
            with open(f'saved_books/{book.book_name}.dat', 'wb') as fh:
                pickle.dump(book, fh)
            return book, f'The book [{book.book_name}] was saved.\n'
        else:
            print(f'\nA book with the name {book.book_name} already exists.\n')
            print('What action do you want to perform?:\n'
                  '1 Enter another name\n'
                  '2 Replace the saved book\n'
                  '3 Cancel save\n')
            user_choice = input('Enter your choice: ')
            if user_choice == '1':
                while True:
                    print('For exit enter: exit\n')
                    new_book_name = input('Enter new name: ')
                    if new_book_name.lower() == 'exit':
                        return book, 'Cancel saving the book...\n'
                    book.change_book_name(new_book_name)
                    if f'{book.book_name}\n' not in books_list:
                        with open('../saved_books/saved_books.txt', 'a') as file_a:
                            file_a.write(f'{book.book_name}\n')
                        with open(f'saved_books/{book.book_name}.dat', 'wb') as fh:
                            pickle.dump(book, fh)
                        return book, f'The book [{book.book_name}] was saved.\n'
                    print(f'\nA book with the name {book.book_name} already exists.\n')
                    print('Try again.\n')
            elif user_choice == '2':
                try:
                    with open(f'saved_books/{book.book_name}.dat', 'wb') as fh:
                        pickle.dump(book, fh)
                    return book, f'The book [{book.book_name}] was rewritten.\n'
                except FileNotFoundError:
                    raise FileNotFoundError('File not found.\n')
            elif user_choice == '3':
                return book, 'Cancel save...\n'
            else:
                return book, 'Unknown command!\nAbort save...'


def load(book):
    all_books = []
    try:
        with open('../saved_books/saved_books.txt', 'r') as fh:
            book_list = fh.readlines()
            print('\nsaved_books:')
            for count, book_name in enumerate(book_list, 1):
                all_books.append(book_name.strip())
                print(f'{count} {book_name}', end='')
    except FileNotFoundError:
        print('\nsaved_books not found.\n')
        user_choice = input('Do you want to create a new book? Y/N: ')
        if user_choice.upper() == 'Y':
            return new()
        elif user_choice.upper() == 'N':
            return book, '\nCancel load...\n'
        else:
            return book, 'Unknown command\nAbort...'

    index = input('\nMake your choice: ')
    if index.isdigit():
        book_file = all_books[int(index) - 1]
    else:
        return book, '\nWrong command.\nAbort loading...\n'
    try:
        with open(f'saved_books/{book_file}.dat', 'rb') as fh:
            book = pickle.load(fh)
            return book, f'\nThe book [{book.book_name}] has been loaded.\n'
    except FileNotFoundError:
        return book, '\nFile not found...\nAbort loading...\n'