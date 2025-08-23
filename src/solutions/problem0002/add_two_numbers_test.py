import pytest

from typing import List

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from structures import to_list, to_array

from add_two_numbers import Solution

cases = [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
]


@pytest.mark.parametrize("l1, l2, expected", cases)
def test_addTwoNumbers(l1: List[int], l2: List[int], expected: List[int]) -> None:
    solution = Solution()

    actual = to_array(solution.addTwoNumbers(to_list(l1), to_list(l2)))

    assert actual == expected


if __name__ == "__main__":
    print("2.两数相加")
    pytest.main(["-v", __file__])
