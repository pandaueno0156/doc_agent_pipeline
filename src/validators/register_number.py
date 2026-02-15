#src

def validate_register_number(register_number: str) -> bool:
    """
    Validate the register number of the receipt.
    """
    # Need T + 13 digits to be a valid register number for taxi


    if len(register_number) != 14:
        return False
    elif not register_number.startswith("T"):
        return False
    elif not register_number[1:].isdigit():
        return False

    return True