from dzvina_assist.Classes import Field
from datetime import datetime, date
import re


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
