def add_tags_func(book):

    name = input('Please enter name: ')
    name = name.strip().title()
    splitter = ''
    if name not in book.data:
        return book, '\n<<< This name not in contact book\n'
    contact = book[name]
    if contact.notes:
        print('\nWhich note do you want to tag?\n')
        for count, note in enumerate(contact.notes, 1):
            print(count, note)
        user_input = input('Choice note: ')
        if user_input.isnumeric() and int(user_input) <= len(contact.notes):
            tags = input('Please write your tags: ')
            for i in tags:
                if not i.isalnum():
                    splitter = i
                    if splitter:
                        break
            try:
                tags = tags.split(splitter)
                tags = [tag.strip().lower() for tag in tags]
            except ValueError:
                tags = [tags]
            contact.add_tags(user_input, tags)
        else:
            return book, '<<< Invalid choice.'
    else:
        return book, f'\n<<< Contact {name} has no notes.\n'

    return book, f'\n<<< Your tags: [{tags}] saved.\n'


def find_tags_func(book):
    tag = input('Please enter tag: ')
    tag = tag.strip().lower()
    result = []
    result_str = '<<< Nothing found...'
    for contact in book.data:
        contact = book.data[contact]
        if contact.notes:
            for note in contact.notes:
                if tag in note.tags:
                    result.append(contact)

    if result:
        result_str = ''
        for contact in result:
            contact_info = contact.get_all_info()
            for key in contact_info:
                if isinstance(contact_info[key], str):
                    result_str += f'{key.title()}: {contact_info[key]}\n'
                elif isinstance(contact_info[key], list):
                    if key == 'phones':
                        result_str += f'{key.title()}: '
                        for value in contact_info[key]:
                            result_str += f'{value}, '
                        result_str += '\b\b\n'
                    elif key == 'notes':
                        result_str += f'{"-" * 30}\n'
                        result_str += f'[{key.title()}]:\n'
                        for count, note in enumerate(contact_info[key], 1):
                            result_str += f'{count}. [{note}]\n'
                else:
                    result_str += f'{key.title()}: {contact_info[key]}\n'

    return result_str
