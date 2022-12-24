

def add_address(data: str):
    name, address = split_data(data)
    if book.name:
        raise ValueError('This user not in contact book')
    if book.address:
        raise ValueError('This contact already exist address')
    record = add_address(address)
    book.add_record(record)
    return f'Address: {address} has been added to contact: {name}'