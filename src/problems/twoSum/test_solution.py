import pytest

from typing import List
from solution import Solution

testdata = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 2], 0, []),
]


@pytest.mark.parametrize("nums,target,expected", testdata)
def test_twoSum(nums: List[int], target: int, expected: List[int]) -> None:
    solution = Solution()

    actual = solution.twoSum(nums, target)
    assert actual == expected
