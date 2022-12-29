from collections import UserDict


class AddressBook(UserDict):

    book_name = None

    def __setitem__(self, key, value):
        if key:
            self.data[key] = value

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def add_record(self, record):
        self.data[str(record.name)] = record

    def del_record(self, name):
        del self.data[name]

    def change_book_name(self, name):
        self.book_name = name

    def find_record(self, name):
        if name in self.data:
            contact = self.data[name]
            phones = contact.get_all_phones()
            return f'\n[{name}]:{phones}\n'
        else:
            return 'Such contact does not exist. Try again!'

    def get_all_contacts(self):
        all_contacts = []
        for name in self.data.keys():
            phones = self.data[name]
            phones = phones.get_all_phones()
            all_contacts.append({name: phones})
        return all_contacts

    def merging_books(self, book):
        self.data = book.update(self.data)
