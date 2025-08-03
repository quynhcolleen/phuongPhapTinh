from decimal import Decimal, ROUND_HALF_UP

def lamTron(val):
    d = Decimal(str(val))
    digits_after_dot = abs(d.as_tuple().exponent)
    if digits_after_dot <= 9:
        return str(d.normalize())
    else:
        rounded = d.quantize(Decimal('1.0000000'), rounding=ROUND_HALF_UP)
        return str(rounded.normalize())
