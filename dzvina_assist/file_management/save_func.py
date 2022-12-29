import pickle


def save_func(save, book):
    if not book.book_name:
        print('For exit enter: exit')
        while True:
            new_book_name = input('Please enter new_book book name: ')
            if new_book_name.lower() == 'exit':
                return save, book, '<<< \033[33mCancel saving the book...\033[0m\n'
            if new_book_name and new_book_name not in save.data:
                book.change_book_name(new_book_name)
                break
            print('<<< \033[33mA book with that name already exists.\033[0m')
            print('Try again.')
    save.data[book.book_name] = book
    with open(f'save.dat', 'wb') as file:
        pickle.dump(save, file)
    return save, book, f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m] was saved.\033[0m\n'
