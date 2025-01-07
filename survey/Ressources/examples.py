def check_value(value):
    if value < 1 or value > 10:
        raise ValueError('Value must be between 1 and 10')