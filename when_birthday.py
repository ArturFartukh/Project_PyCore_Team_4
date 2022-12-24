from datetime import datetime, date
import Birthday
import Record


def days_before_birthday(data: str):
    name = data.strip().title()
    if name not in book:
        raise ValueError('No such contact found!')
    record = book[name]
    result = record.days_to_birthday()
    return result
