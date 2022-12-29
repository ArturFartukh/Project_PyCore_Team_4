from dzvina_assist.support_funcs import phone_validator


def search_contact_global_func(save):
    name = None
    phone = None
    result = []
    result_str = '<<< Nothing found...\n'
    data = input('Please enter name or phone: ')
    data = data.strip()
    if data[0].isalpha():
        name = data.strip().title()
    elif data[0].isdigit() or data[0] == '+':
        phone = phone_validator(data)
    else:
        return '\n<<< Unknown data\n'

    if name:
        for book in save.data:
            book = save.data[book]
            if name in book.data:
                contact_info = book.find_record(name)
                if contact_info not in result:
                    result.append(contact_info)
    elif phone:
        for book in save.data:
            book = save.data[book]
            for contacts in book.get_all_contacts():
                for name, phones in contacts.items():
                    if phone in phones:
                        contact_info = book.find_record(name)
                        if contact_info not in result:
                            result.append(contact_info)
    if result:
        result_str = ''
        for contact in result:
            result_str += f'{contact}\n'

    return result_str
