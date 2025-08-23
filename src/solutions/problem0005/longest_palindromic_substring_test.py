import pytest

from longest_palindromic_substring import Solution

cases = [
    ("babad", "bab"),
    ("cbbd", "bb"),
]


@pytest.mark.parametrize("s, expected", cases)
def test_longestPalindrome(s: str, expected: str) -> None:
    solution = Solution()

    actual = solution.longestPalindrome(s)

    assert actual == expected


if __name__ == "__main__":
    print("5.最长回文子串")
    pytest.main(["-v", __file__])
