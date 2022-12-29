from dzvina_assist.Classes import Field
import re


class Address(Field):
    """Address parser"""
    @Field.value.setter
    def address_parser(self, value):
        address = re.findall(r'\w+', value)
        if not address:
            return
        self._value = address
