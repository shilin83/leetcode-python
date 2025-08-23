class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        # * 从中心向两边扩散
        def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
            # * 当左右指针在边界内且对应字符相等，继续扩展
            while 0 <= left and right < length and s[left] == s[right]:
                left -= 1
                right += 1

            # * 返回回文子串的左右边界
            return left + 1, right - 1

        # * 初始回文子串的左右边界
        start, end = 0, 0

        for i in range(length):
            # * 奇数长度回文串
            left1, right1 = expandAroundCenter(i, i)

            # * 偶数长度回文串
            left2, right2 = expandAroundCenter(i, i + 1)

            # * 更新回文子串的左右边界
            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start : end + 1]
