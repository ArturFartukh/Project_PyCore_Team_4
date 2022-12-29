from datetime import date
from dzvina_assist.Classes import Name, Phone, Address, Email, Birthday, Note


class Record:
    """Contact information"""
    def __init__(self, new_name, phone=None):
        """Initialization of an instance of a class"""
        self.name = Name(new_name)
        self.phones = None
        if phone:
            self.add_phone(phone)
        self.address = None
        self.email = None
        self.birthday = None
        self.notes = None

    def add_phone(self, new_phone: str):
        """Adds a phone number"""
        if not self.phones:
            self.phones = [Phone(new_phone)]
        else:
            self.phones.append(Phone(new_phone))

    def change_phone(self, choice: str, new: str):
        """Changes the phone number"""
        index = int(choice) - 1
        self.phones[index] = Phone(new)

    def del_phone(self, del_phone: str):
        """Deletes a phone number"""
        for phone in self.phones:
            if phone.value == del_phone:
                self.phones.remove(phone)

    def add_address(self, address_data: str):
        """Adds an address"""
        self.address = Address(address_data)
        if not self.address:
            return False
        return True

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

    def next_birthday(self):
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
            return f'{difference.days} days.'
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
        index = int(note_number) - 1
        self.notes[index] = Note(note_data)

    def del_note(self, note_number: str):
        """Deletes the selected note"""
        index = int(note_number) - 1
        self.notes.remove(self.notes[index])

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
        index = int(note_number) - 1
        note = self.notes[index]
        note.tags = None

    def get_all_phones(self) -> list:
        """Returns a list of all phone numbers for a contact"""
        return [number.value for number in self.phones]

    def has_phone(self, phone: str) -> bool:
        """Checks whether the specified number is in the list of contact numbers.
        Returns True or False"""
        if self.phones:
            for number in self.phones:
                if number.value == phone:
                    return True
        return False

    def get_all_info(self) -> dict:
        """Returns a dictionary with all information about the contact"""
        user_data = {'name': self.name.value}
        if self.phones:
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
