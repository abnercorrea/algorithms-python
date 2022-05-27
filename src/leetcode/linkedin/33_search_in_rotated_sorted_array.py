import pytest
from typing import List


def search_rotated_array(nums: List[int], target: int) -> int:
    begin, end = 0, len(nums) - 1

    while begin <= end:
        mid = (begin + end) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[begin]:
            if nums[begin] <= target < nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                begin = mid + 1
            else:
                end = mid -1

    return -1


def test_search_rotated_array():
    assert search_rotated_array([4,5,6,7,1,2,3], 1) == 4
    assert search_rotated_array([4,5,6,7,1,2,3], 4) == 0
    assert search_rotated_array([5,1,3], 5) == 0
    assert search_rotated_array([5,1,3], 3) == 2
    assert search_rotated_array([5,1,3], 3) == 2


if __name__ == '__main__':
    pytest.main()
