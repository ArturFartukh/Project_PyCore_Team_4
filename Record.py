from datetime import date
import Name
from phone_address_email import *
from birthday_note import *


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
        bd_in_year = self.birthday
        bd_in_year = bd_in_year.replace(year=date.today().year)
        if bd_in_year > date.today():
            difference = bd_in_year - date.today()
            return difference.days
        elif bd_in_year < date.today():
            difference = bd_in_year.replace(year=date.today().year + 1) - date.today()
            return difference.days
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
            raise IndexError
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
