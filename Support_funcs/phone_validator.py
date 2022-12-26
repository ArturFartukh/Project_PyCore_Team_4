def phone_validator(phone: str) -> str:
    """Analyzes and changes the phone number according to the template: '+123456789123'"""
    if len(phone) == 13 and phone[0] != '+' and not phone[1:].isdigit():
        raise ValueError('Wrong phone!')
    elif len(phone) == 10 and not phone.isdigit():
        raise ValueError('Wrong phone!')
    elif not 10 <= len(phone) <= 13:
        raise ValueError('Wrong phone!')
    elif len(phone) == 10:
        phone = '+38' + phone
    elif len(phone) == 11:
        phone = '+3' + phone
    elif len(phone) == 10:
        phone = '+38' + phone
    elif len(phone) == 12:
        phone = '+' + phone
    return phone
