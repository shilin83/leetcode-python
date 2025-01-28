from typing import List

import pytest

from twoSum import Solution

testdata = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([], 0, []),
]


@pytest.mark.parametrize("nums, target, expected", testdata)
def test_twoSum(nums: List[int], target: int, expected: List[int]) -> None:
    solution = Solution()

    assert solution.twoSum(nums, target) == expected
