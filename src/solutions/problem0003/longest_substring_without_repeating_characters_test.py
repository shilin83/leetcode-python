import pytest

from longest_substring_without_repeating_characters import Solution

cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]


@pytest.mark.parametrize("s, expected", cases)
def test_lengthOfLongestSubstring(s: str, expected: int) -> None:
    solution = Solution()

    actual = solution.lengthOfLongestSubstring(s)

    assert actual == expected


if __name__ == "__main__":
    print("3.无重复字符的最长子串")
    pytest.main(["-v", __file__])
