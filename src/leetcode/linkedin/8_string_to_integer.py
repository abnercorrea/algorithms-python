import pytest


def my_atoi(s: str) -> int:
    if not s:
        return 0
    i = 0
    length = len(s)
    while i < length and s[i] == ' ':
        i += 1
    if i == length:
        return 0
    sign = -1 if s[i] == '-' else 1
    if s[i] in ['-', '+']:
        i += 1
    x = 0
    max_int = 1 << 31
    while i < length and '0' <= s[i] <= '9' and x < max_int:
        x = (x * 10) + int(s[i])
        i += 1
    x *= sign
    x = min(max(x, -max_int), max_int - 1)
    return x


def test_myatoi():
    assert my_atoi('42') == 42
    assert my_atoi('-42') == -42
    assert my_atoi('    200') == 200
    assert my_atoi('  +35ABC') == 35
    assert my_atoi('10000000000000') == (1 << 31) - 1
    assert my_atoi('-10000000000000') == -(1 << 31)
    assert my_atoi('') == 0
    assert my_atoi(None) == 0


if __name__ == '__main__':
    pytest.main()
