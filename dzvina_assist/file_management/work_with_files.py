from dzvina_assist.Classes import AddressBook
import pickle


def new(book):
    print('For exit enter: exit')
    book_name = input('Enter new book name: ')
    if book_name.lower() == 'exit':
        return book, '<<< \033[33mCancellation of book creation...\033[0m\n'
    book_name = book_name.strip()
    book = AddressBook()
    book.change_book_name(book_name)
    return book, f'<<< \033[32mA new book [\033[1m{book_name}\033[0m\033[32m] has been created.\033[0m'


def save(book):

    if not book.book_name:
        print('This is a new book.\n')
        new_book_name = input('Please enter new book name: ')
        book.change_book_name(new_book_name)

    with open('saved_books/saved_books.txt', 'r') as file_r:
        books_list = file_r.readlines()
        if f'{book.book_name}\n' not in books_list:
            with open('saved_books/saved_books.txt', 'a') as file_a:
                file_a.write(f'{book.book_name}\n')
            with open(f'saved_books/{book.book_name}.dat', 'wb') as fh:
                pickle.dump(book, fh)
            return book, f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m] was saved.\033[0m\n'
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
                        return book, '<<< \033[33mCancel saving the book...\033[0m\n'
                    book.change_book_name(new_book_name)
                    if f'{book.book_name}\n' not in books_list:
                        with open('saved_books/saved_books.txt', 'a') as file_a:
                            file_a.write(f'{book.book_name}\n')
                        with open(f'saved_books/{book.book_name}.dat', 'wb') as fh:
                            pickle.dump(book, fh)
                        return book, f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m] ' \
                                     f'was saved.\033[0m\n'
                    print(f'\nA book with the name {book.book_name} already exists.\n')
                    print('Try again.\n')
            elif user_choice == '2':
                try:
                    with open(f'saved_books/{book.book_name}.dat', 'wb') as fh:
                        pickle.dump(book, fh)
                    return book, f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m]' \
                                 f' was rewritten.\033[0m\n'
                except FileNotFoundError:
                    return book, '<<< \033[31mFile not found.\033[0m\n'
            elif user_choice == '3':
                return book, '<<< \033[33mCancel save...\033[0m\n'
            else:
                return book, '<<< \033[31mUnknown command!\n<<< Abort save...\033[0m\n'


def load(book):
    all_books = []
    try:
        with open('saved_books/saved_books.txt', 'r') as fh:
            book_list = fh.readlines()
            if not book_list:
                return book, '<<< \033[33mThere are no saved phone books.\033[0m\n'
            print('\nsaved_books:')
            for count, book_name in enumerate(book_list, 1):
                all_books.append(book_name.strip())
                print(f'{count} {book_name}', end='')
    except FileNotFoundError:
        print('\nsaved_books not found.\n')
        user_choice = input('Do you want to create a new book? Y/N: ')
        if user_choice.upper() == 'Y':
            return new(book)
        elif user_choice.upper() == 'N':
            return book, '<<< \033[33mCancel load...\033[0m\n'
        else:
            return book, '<<< \033[31mUnknown command\n<<< Abort...\033[0m\n'

    index = input('\nMake your choice: ')
    if index.isdigit():
        book_file = all_books[int(index) - 1]
    else:
        return book, '<<< \033[31mWrong command.\n<<< Abort loading...\033[0m\n'
    try:
        with open(f'saved_books/{book_file}.dat', 'rb') as fh:
            book = pickle.load(fh)
            return book, f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m] has been loaded.\033[0m\n'
    except FileNotFoundError:
        return book, '<<< \033[31mFile not found...\n<<< Abort loading...\033[0m\n'
