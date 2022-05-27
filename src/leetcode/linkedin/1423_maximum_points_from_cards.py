import pytest
from typing import List


def calculate_max_score(cardPoints: List[int], k: int) -> int:
    left = 0
    right = 0
    n = len(cardPoints)

    for i in range(k):
        right += cardPoints[n - i - 1]

    max_score = right

    for i in range(k):
        left += cardPoints[i]
        right -= cardPoints[n - k + i]
        max_score = max(max_score, left + right)

    return max_score


def test_calculate_max_score():
    assert calculate_max_score([1,2,3,4,5,6,1], 3) == 12
    assert calculate_max_score([2,2,2], 2) == 4
    assert calculate_max_score([9,7,7,9,7,7,9], 7) == 55
    assert calculate_max_score([96,90,41,82,39,74,64,50,30], 8) == 536


if __name__ == '__main__':
    pytest.main()
