def all_numbers_func(book) -> str:
    """Displays the entire phonebook."""

    if not book.data:
        return f'<<< The address book has no contacts yet.'

    result = ''

    phone_book = book.get_all_contacts()

    for contact in phone_book:
        for name in contact:
            result += f'{"-" * 16}\n' + f'{name}:\n'
            for number in contact[name]:
                result += '{:<15}|\n'.format(number)

    if result:
        return result + f'{"-" * 16}\n'
