from BookClasses import *


def find_tags(tags: str):
    if tags not in book.data.keys():
        raise ValueError('This tags not found')
    if book.notes:
        for count, item in enumerate(book.notes, 1):
            return f'Tags found: {count}, {item[tags]}'

