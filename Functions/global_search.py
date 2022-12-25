import pickle


def global_searsh(data: str):
    name = None
    phone = None
    result = []
    if data[0].isalpha():
        name = data.strip().lower()
    elif data[0].isdigit() or data[0] == '+':
        phone = data
    else:
        raise ValueError('Unknown data')

    if name:
        with open('./Saved books/saved_books.txt', 'r') as file_r:
            for book in file_r.readlines():
                with open(f'./Saved books/{book.strip()}.dat', 'rb') as file_rb:
                    search_book = pickle.load(file_rb)
                    for contact in search_book.data:
                        if name in contact.lower():
                            result.append(search_book.find_contact(contact))
    elif phone:
        with open('./Saved books/saved_books.txt', 'r') as file_r:
            for book in file_r.readlines():
                with open(f'./Saved books/{book.strip()}.dat', 'rb') as file_rb:
                    search_book = pickle.load(file_rb)
                    for contact in search_book.get_all_contacts():
                        for numbers in contact.values():
                            for number in numbers:
                                if phone in number and contact not in result:
                                    result.append(contact)

    for i in result:
        print(i)

    return '-' * 30
