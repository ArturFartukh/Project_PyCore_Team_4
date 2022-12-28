def save_func(save, book):
    if not book.book_name:
        print('For exit enter: exit')
        while True:
            new_book_name = input('Please enter new_book book name: ')
            if new_book_name.lower() == 'exit':
                return save, book, '<<< \033[33mCancel saving the book...\033[0m\n'
            if new_book_name:
                book.change_book_name(new_book_name)
                break
            print('Try again.')
    if book.book_name not in save.data:
        save.data[book.book_name] = book
        return save, book, f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m] was saved.\033[0m\n'

    print(f'\nA book with the name {book.book_name} already exists.\n')
    print('What action do you want to perform?:\n'
          '1 Enter another name\n'
          '2 Replace the saved book\n'
          '3 Cancel save_func\n')
    user_choice = input('Enter your choice: ')
    if not user_choice.isdigit() or not 0 < int(user_choice) <= 3:
        return save, book, '<<< \033[31mWrong choice!\n<<< Abort save...\033[0m\n'

    if user_choice == '1':
        print('For exit enter: exit')
        while True:
            new_book_name = input('Please enter new_book book name: ')
            if new_book_name.lower() == 'exit':
                return save, book, '<<< \033[33mCancel saving the book...\033[0m\n'
            if new_book_name != book.book_name:
                book = book.change_book_name(new_book_name)
                save.data[book.book_name] = book
            print('Try again.')
    elif user_choice == '2':
        save.data[book.book_name] = book
        return save, book, f'<<< \033[32mThe book [\033[1m{book.book_name}\033[0m\033[32m]' \
                           f' was rewritten.\033[0m\n'
    elif user_choice == '3':
        return save, book, '<<< \033[33mCancel save...\033[0m\n'
