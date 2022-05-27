import pytest


def int_to_roman(num: int) -> str:
    s = str(num)
    p = 1
    roman = ''

    for i in range(len(s), 0, -1):
        d = int(s[i - 1])

        if p == 1:
            unit, five, ten = 'I', 'V', 'X'
        elif p == 10:
            unit, five, ten = 'X', 'L', 'C'
        elif p == 100:
            unit, five, ten = 'C', 'D', 'M'
        elif p == 1000:
            unit, five, ten = 'M', '', ''

        if 1 <= d <= 3:
            roman = (unit * d) + roman
        elif d == 4:
            roman = unit + five + roman
        elif d == 5:
            roman = five + roman
        elif 6 <= d <= 8:
            roman = five + (unit * (d - 5)) + roman
        elif d == 9:
            roman = unit + ten + roman

        p *= 10

    return roman


def test_int_to_roman():
    assert int_to_roman(10) == 'X'
    assert int_to_roman(3999) == 'MMMCMXCIX'
    assert int_to_roman(100) == 'C'
    assert int_to_roman(3) == 'III'
    assert int_to_roman(444) == 'CDXLIV'
    assert int_to_roman(999) == 'CMXCIX'


if __name__ == "__main__":
    pytest.main()