import pytest

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    combinations = []

    def combination_rec(start: int, comb_sum: int, combination: List[int]):
        if comb_sum == target:
            combinations.append(combination.copy())
            return

        if comb_sum > target:
            return

        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            combination_rec(i, comb_sum + candidates[i], combination)
            combination.pop()

    combination_rec(0, 0, [])

    return combinations


def test_combination_sum():
    assert sorted(combination_sum([42], 42)) == sorted([[42]])
    assert sorted(combination_sum([1,2,3], 3)) == sorted([[1,1,1],[1,2],[3]])
    assert sorted(combination_sum([2,4], 7)) == sorted([])
    assert sorted(combination_sum([], 1)) == sorted([])


if __name__ == '__main__':
    pytest.main()

