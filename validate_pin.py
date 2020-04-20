def validate_pin(pin):
    if (len(pin) == 4) or (len(pin) == 6):
        pin_bool = pin.isdigit()
        return pin_bool
    else:
        return False