from datetime import datetime
import re

class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        pattern = r'\d{2}\.\d{2}\.\d{4}'
        result = re.fullmatch(pattern, value)
        if not result:
            raise ValueError('Wrong birthday date. Please, input DD.MM.YYYY')
        birthday_date = datetime.strptime(value, '%d.%m.%Y').date()
        if birthday_date > date.today():
            raise ValueError('Birthday must be less than current year and date')
        self._value = value


class Note(Field):
    pass
