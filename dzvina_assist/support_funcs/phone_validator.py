def phone_validator(phone: str) -> str:
    """Analyzes and changes the phone number according to the template: '+123456789123'"""
    valid_phone = ''
    if len(phone) == 10 and phone[0] != '+':
        valid_phone = '+38' + phone
    elif len(phone) == 11 and phone[0] != '+':
        valid_phone = '+3' + phone
    elif len(phone) == 12 and phone[0] != '+':
        valid_phone = '+' + phone
    elif len(phone) == 13 and phone[0] == '+':
        valid_phone = phone
    return valid_phone
