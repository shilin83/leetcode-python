import pytest

from typing import List
from .solution import Solution
from ...structures.LinkedList import arrayToList, listToArray

testdata = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
]


@pytest.mark.parametrize("l1,l2,expected", testdata)
def test_addTwoNumbers(l1: List[int], l2: List[int], expected: List[int]) -> None:
    solution = Solution()

    actual = solution.addTwoNumbers(arrayToList(l1), arrayToList(l2))
    assert listToArray(actual) == expected
