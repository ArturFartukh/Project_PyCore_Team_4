from datetime import date, datetime
import re
import Field


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
        self.__tags = None

    @property
    def tags(self):
        return self.__tags

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
        self.__tags = new_tags
