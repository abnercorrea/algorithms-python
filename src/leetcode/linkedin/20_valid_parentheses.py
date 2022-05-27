import pytest


def is_valid_parentheses(s: str) -> bool:
    if not s:
        return True

    open_stack = []

    for c in s:
        if c in [')', ']', '}']:
            if not open_stack:
                return False
            o = open_stack.pop()
            if (c == ')' and o != '(') or (c == ']' and o != '[') or (c == '}' and o != '{'):
                return False
        else:
            open_stack.append(c)

    return len(open_stack) == 0


def test_is_valid_parentheses():
    assert is_valid_parentheses('()')
    assert is_valid_parentheses('([])')
    assert is_valid_parentheses('([{()}]){}[]()')
    assert is_valid_parentheses('')
    assert is_valid_parentheses(None)
    assert not is_valid_parentheses('(')
    assert not is_valid_parentheses(']')
    assert not is_valid_parentheses('()]')
    assert not is_valid_parentheses('(])')
    assert not is_valid_parentheses('([]){')


if __name__ == '__main__':
    pytest.main()
