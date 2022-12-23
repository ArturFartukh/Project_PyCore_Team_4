import Field
import re


class Phone(Field):
    """Make a regular expression for validating a Phone"""
    @Field.value.setter
    def value(self, value):
        pattern = r'\+\d{12}'
        phone = re.findall(pattern, value)
        if not phone:
            raise ValueError('Phone must look like +123456789123')
        self._value = phone


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
