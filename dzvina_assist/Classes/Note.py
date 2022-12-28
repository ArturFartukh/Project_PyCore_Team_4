from dzvina_assist.Classes import Field


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
