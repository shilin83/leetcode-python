import pytest

from src.solutions.longestSubstringWithoutRepeatingCharacters import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ],
)
def test_lengthOfLongestSubstring(s, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected
