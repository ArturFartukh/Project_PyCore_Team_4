from dzvina_assist.Classes import Field


class Name(Field):
    @Field.value.setter
    def value(self, value: str):
        if not value.isalpha():
            raise ValueError('Incorrect name!')
        if value[0].isdigit():
            raise ValueError('The name cannot start with a number!')
        self._value = value
