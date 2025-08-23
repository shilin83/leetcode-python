import pytest

from typing import List

from median_of_two_sorted_arrays import Solution

cases = [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
]


@pytest.mark.parametrize("nums1, nums2, expected", cases)
def test_findMedianSortedArrays(nums1: List[int], nums2: List[int], expected: float) -> None:
    solution = Solution()

    actual = solution.findMedianSortedArrays(nums1, nums2)

    assert actual == expected


if __name__ == "__main__":
    print("4.寻找两个正序数组的中位数")
    pytest.main(["-v", __file__])
