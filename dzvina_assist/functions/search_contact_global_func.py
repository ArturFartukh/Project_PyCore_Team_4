from support_funcs import phone_validator
import pickle


def search_contact_global_func(data: str):
    name = None
    phone = None
    result = []
    result_str = '<<< Nothing found...'
    if data[0].isalpha():
        name = data.strip().title()
    elif data[0].isdigit() or data[0] == '+':
        phone = phone_validator(data)
    else:
        return '\n<<< Unknown data\n'

    if name:
        with open('./saved_books/saved_books.txt', 'r') as file_r:
            for book in file_r.readlines():
                with open(f'./saved_books/{book.strip()}.dat', 'rb') as file_rb:
                    search_book = pickle.load(file_rb)
                    for contact in search_book.data:
                        if name in contact:
                            contact_info = search_book.find_record(contact)
                            if contact_info not in result:
                                result.append(contact_info)
    elif phone:
        with open('./saved_books/saved_books.txt', 'r') as file_r:
            for book in file_r.readlines():
                with open(f'./saved_books/{book.strip()}.dat', 'rb') as file_rb:
                    search_book = pickle.load(file_rb)
                    for contacts in search_book.get_all_contacts():
                        for key, numbers in contacts.items():
                            if phone in numbers:
                                contact_info = search_book.find_record(key)
                                if contact_info not in result:
                                    result.append(contact_info)
    if result:
        result_str = ''
        for contact in result:
            result_str += f'{contact}\n'

    return result_str
