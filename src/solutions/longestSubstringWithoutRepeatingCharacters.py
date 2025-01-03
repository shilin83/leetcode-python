class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        left, right, max_len = 0, 0, 0

        while right < len(s):
            # * 如果哈希表中存在当前元素，则移动滑动窗口的左边界到当前元素的下一个位置
            char = s[right]
            if char in hash_table:
                left = max(left, hash_table[char] + 1)

            # * 将当前元素及其索引存入哈希表
            # * 移动滑动窗口的右边界
            # * 计算滑动窗口的最大长度
            hash_table[char] = right
            right += 1
            max_len = max(max_len, right - left)

        return max_len
