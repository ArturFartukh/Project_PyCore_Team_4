from functions.address_func import add_address_func, change_address_func
from functions.all_contact_info_func import all_contact_info_func
from functions.all_numbers_func import all_numbers_func
from functions.birthday_func import add_birthday_func, days_before_birthday_func
from functions.contact_func import add_func, change_phone_func, del_func
from functions.contact_info_func import contact_info_func
from functions.email_func import add_email_func, change_email_func
from functions.note_func import add_note_func, change_notes_func, del_note_func, search_in_notes_func
from functions.search_contact_func import search_contact_func
from functions.search_contact_global_func import search_contact_global_func
from functions.tags_fгnc import add_tags_func, find_tags_func
from functions.interactive import start

__all__ = ['start',
           'add_address_func',
           'change_address_func',
           'all_contact_info_func',
           'all_numbers_func',
           'add_birthday_func',
           'days_before_birthday_func',
           'add_func',
           'change_phone_func',
           'del_func',
           'contact_info_func',
           'add_email_func',
           'change_email_func',
           'add_note_func',
           'change_notes_func',
           'del_note_func',
           'search_in_notes_func',
           'search_contact_func',
           'search_contact_global_func',
           'add_tags_func',
           'find_tags_func'
           ]

print('Loading functions...')
