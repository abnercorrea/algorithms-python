import pytest
from typing import Dict


def count_char(s: str) -> Dict[str, int]:
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def min_steps(s: str, t: str) -> int:
    s_counts = count_char(s)
    t_counts = count_char(t)
    steps = 0
    for c, count in s_counts.items():
        steps += max(count - t_counts.get(c, 0), 0)
    return steps


def test_min_steps():
    assert min_steps('bab', 'aba') == 1


if __name__ == '__main__':
    pytest.main()
