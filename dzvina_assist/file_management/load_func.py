def load_func(save):
    if not save.data:
        return '<<< \033[33mThere are no saved phone books.\033[0m\n'
    print('\nsaved_books:')
    for count, book_name in enumerate(save.data, 1):
        print(f'{count} {book_name}')
    index = input('\nMake your choice: ')
    if int(index) <= len(save.data):
        for count, book_name in enumerate(save.data, 1):
            if count == int(index):
                book = save.data[book_name]
                return book
    else:
        return '<<< \033[31mWrong command.\n<<< Abort loading...\033[0m\n'
