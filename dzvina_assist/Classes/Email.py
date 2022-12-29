from dzvina_assist.Classes import Field
import re


class Email(Field):
    """Make a regular expression for validating an Email"""
    @Field.value.setter
    def check_email(self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = re.findall(pattern, value)
        if not email:
            raise ValueError('Invalid Email')
        self._value = email
