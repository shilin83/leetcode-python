import pytest

from typing import List

from two_sum import Solution

cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


@pytest.mark.parametrize("nums, target, expected", cases)
def test_twoSum(nums: List[int], target: int, expected: List[int]) -> None:
    solution = Solution()

    actual = solution.twoSum(nums, target)

    assert actual == expected


if __name__ == "__main__":
    print("1.两数之和")
    pytest.main(["-v", __file__])
