import pytest

from src.solutions.addTwoNumbers import Solution
from src.structures.linkedList import int2List


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_addTwoNumbers(nums1, nums2, expected):
    solution = Solution()

    expected = int2List(expected)
    actual = solution.addTwoNumbers(int2List(nums1), int2List(nums2))

    while expected is not None and actual is not None:
        assert actual.val == expected.val
        expected = expected.next
        actual = actual.next
