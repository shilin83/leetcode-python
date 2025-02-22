from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for key, value in enumerate(nums):
            # * 计算目标值与当前元素的差值
            diff = target - value

            # * 如果哈希表中存在差值，则返回差值与当前元素的索引
            if diff in hash_table:
                return [hash_table[diff], key]

            # * 将当前元素及其索引存入哈希表
            hash_table[value] = key

        return []
