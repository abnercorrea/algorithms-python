import pytest
from typing import List, Tuple


def roman_symbol_values() -> List[Tuple[str, int]]:
    roman_symbols = [
        ('I', 'V'),
        ('X', 'L'),
        ('C', 'D'),
        ('M', ''),
    ]

    symbol_values = []
    base10 = 1

    for i in range(len(roman_symbols)):
        one, five = roman_symbols[i]

        if i < len(roman_symbols) - 1:
            ten = roman_symbols[i + 1][0]
            symbol_values.append((one + ten, 9 * base10))
        if five:
            symbol_values.append((one + five, 4 * base10))
            symbol_values.append((five, 5 * base10))
        symbol_values.append((one * 3, 3 * base10))
        symbol_values.append((one * 2, 2 * base10))
        symbol_values.append((one, base10))

        base10 *= 10

    return symbol_values


def roman_to_int(roman: str, symbol_values: List[Tuple[str, int]] = None) -> int:
    i = 0

    for symbol, value in symbol_values or roman_symbol_values():
        if symbol in roman:
            i += value
            roman = roman.replace(symbol, '')

    return i


def test_roman_to_int():
    assert roman_to_int('') == 0
    assert roman_to_int('I') == 1
    assert roman_to_int('II') == 2
    assert roman_to_int('III') == 3
    assert roman_to_int('IV') == 4
    assert roman_to_int('IX') == 9
    assert roman_to_int('MMMCMXCIX') == 3999


if __name__ == '__main__':
    pytest.main()
