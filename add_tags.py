import Record, Note


def add_tags(name: str):
    name = split_data(name)
    if name not in book.data.keys():
        raise ValueError('This name not in contact book')
    if book.name:
        for count, item in enumerate(note, 1):
            print(count, item)
        user_input = input('Choice note #')
        if user_input.isnumeric() and int(user_input) < len(note):
            raise ValueError('Please choice note #')
        u_input = input('Please write your tags: ')
        result = add_tags(u_input)
    return f'Your tags: {result} saved'








