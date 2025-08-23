class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table, max_len, left = {}, 0, 0

        for right, char in enumerate(s):
            # * 如果哈希表中存在当前元素，则移动滑动窗口左边界到当前字符的下一个位置
            if left <= (idx := hash_table.get(char, -1)):
                left = idx + 1

            # * 将当前元素及其索引存入哈希表
            hash_table[char] = right

            # * 移动滑动窗口右边界
            right += 1

            # * 计算滑动窗口最大长度
            max_len = max(max_len, right - left)

        return max_len
