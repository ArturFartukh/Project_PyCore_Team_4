from datetime import datetime, date
from collections import UserDict
import re


class AddressBook(UserDict):
    def __setitem__(self, key, value):
        if key:
            self.data[key] = value

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    book_name = None

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


class Record:
    """Contact information"""
    def __init__(self, new_name, phone=None):
        """Initialization of an instance of a class"""
        if phone is None:
            phone = 'There are no phone numbers.'
        self.name = Name(new_name)
        self.phones = [Phone(phone)]
        self.address = None
        self.email = None
        self.birthday = None
        self.notes = None

    def add_phone(self, new_phone: str):
        """Adds a phone number"""
        if len(self.phones) == 1 and self.phones[0] == 'There are no phone numbers.':
            self.phones[0] = Phone(new_phone)
        else:
            self.phones.append(Phone(new_phone))

    def change_phone(self, old: str, new: str):
        """Changes the phone number"""
        for number in self.phones:
            if number.value == old:
                number.value = new

    def del_phone(self, del_phone: str):
        """Deletes a phone number"""
        for phone in self.phones:
            if phone.value == del_phone:
                self.phones.remove(phone)

    def add_address(self, address_data: str):
        """Adds an address"""
        self.address = Address(address_data)

    def del_address(self):
        """Deletes the address"""
        self.address = None

    def add_email(self, email_data: str):
        """Adds an email address"""
        self.email = Email(email_data)

    def del_email(self):
        """Deletes an email address"""
        self.email = None

    def add_birthday(self, birth_date: str):
        """Adds date of birth"""
        self.birthday = Birthday(birth_date)

    def del_birthday(self):
        """Deletes the date of birth"""
        self.birthday = None

    def days_to_birthday(self):
        """Returns the number of days until the birthday"""
        if not self.birthday:
            return f'Date of birth not specified.'
        bd_in_year = self.birthday.value
        bd_in_year = bd_in_year.replace(year=date.today().year)
        if bd_in_year > date.today():
            difference = bd_in_year - date.today()
            return f'\n{self.name} birthday, after {difference.days} days.\n'
        elif bd_in_year < date.today():
            difference = bd_in_year.replace(year=date.today().year + 1) - date.today()
            return f'\n{self.name} birthday, after {difference.days} days.\n'
        else:
            return f"Today is {self.name.value}'s birthday!"

    def add_note(self, note_data: str):
        """Adds a note"""
        if not self.notes:
            self.notes = [Note(note_data)]
        else:
            self.notes.append(Note(note_data))

    def change_note(self, note_number: str, note_data: str):
        """Changes the selected note"""
        if len(self.notes) < int(note_number):
            raise IndexError
        else:
            index = int(note_number) - 1
            self.notes[index] = Note(note_data)

    def del_note(self, note_number: str):
        """Deletes the selected note"""
        if len(self.notes) < int(note_number):
            raise IndexError
        else:
            index = int(note_number) - 1
            remove_note = self.notes[index]
            self.notes.remove(remove_note)

    def add_tags(self, note_number: str, tags_data: str):
        """Adds tags to the selected note"""
        if len(self.notes) < int(note_number):
            raise 'Note number out of range.'
        else:
            index = int(note_number) - 1
            note = self.notes[index]
            note.tags = tags_data

    def del_tags(self, note_number: str):
        """Removes tags from the selected note"""
        if len(self.notes) < int(note_number):
            raise IndexError
        else:
            index = int(note_number) - 1
            note = self.notes[index]
            note.tags = None

    def get_all_phones(self) -> list:
        """Returns a list of all phone numbers for a contact"""
        return [number.value for number in self.phones]

    def phone_in_contact(self, phone: str) -> bool:
        """Checks whether the specified number is in the list of contact numbers.
        Returns True or False"""
        for number in self.phones:
            if number.value == phone:
                return True
        return False

    def get_all_info(self) -> dict:
        """Returns a dictionary with all information about the contact"""
        user_data = dict()
        user_data['name'] = self.name.value
        user_data['phones'] = self.get_all_phones()
        if self.address:
            user_data['address'] = self.address.value
        if self.email:
            user_data['email'] = self.email.value
        if self.birthday:
            user_data['birthday'] = self.birthday.value
        if self.notes:
            user_data['notes'] = [note.value for note in self.notes]
        return user_data


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value 

    def __str__(self):
        return f'{self._value}'


class Name(Field):
    @Field.value.setter
    def value(self, value: str):
        if not value.isalpha():
            raise ValueError('Incorrect name!')
        if value[0].isdigit():
            raise ValueError('The name cannot start with a number!')
        self._value = value


class Phone(Field):
    """Make a regular expression for validating a Phone"""
    @Field.value.setter
    def value(self, value):
        if value == 'There are no phone numbers.':
            self._value = value
        else:
            pattern = r'\+\d{12}'
            phone = re.findall(pattern, value)
            if phone:
                self._value = phone[0]


class Address(Field):
    """Address parser"""
    @Field.value.setter
    def address_parser(self, value):
        address = re.findall(r'\w+', value)
        if not address:
            raise ValueError('This is really address?')
        self._value = address


class Email(Field):
    """Make a regular expression for validating an Email"""
    @Field.value.setter
    def check_email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = re.findall(pattern, value)
        if not email:
            raise ValueError('Invalid Email')
        self._value = email


class Birthday(Field):

    @Field.value.setter
    def value(self, value: str):
        pattern = r'\d{2}\.\d{2}\.\d{4}'
        result = re.fullmatch(pattern, value)
        if not result:
            raise ValueError('Wrong birthday date. Please, input DD.MM.YYYY')
        birthday_date = datetime.strptime(value, '%d.%m.%Y').date()
        if birthday_date > date.today():
            raise ValueError('Birthday must be less than current year and date')
        self._value = birthday_date


class Note(Field):

    def __init__(self, value: str):
        super().__init__(value)
        self._tags = None

    @Field.value.setter
    def value(self, value: str):
        self._value = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags: str):
        new_tags = []
        tag = ''
        for element in tags:
            if element.isalpha() or element.isnumeric():
                tag += element
            elif not element.isalpha() and not element.isnumeric() and tag:
                new_tags.append(tag)
                tag = ''
            elif not element.isalpha() and not element.isnumeric() and not tag:
                continue
        self._tags = new_tags
