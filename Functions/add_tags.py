import Record, Note


def add_tags(name: str):
    name = split_data(name)
    if name not in book.data.keys():
        raise ValueError('This name not in contact book')
    if book.notes:
        for count, item in enumerate(book.notes, 1):
            print(count, item)
        user_input = input('Choice note #')
        if user_input.isnumeric() and int(user_input) < len(book.notes):
            u_input = input('Please write your tags: ')
            result = add_tags(user_input, u_input)
        else:
            raise ValueError('Please choice note #')
        
    return f'Your tags: {u_input} saved'
