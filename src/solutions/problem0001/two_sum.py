from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i, num in enumerate(nums):
            # * 如果哈希表中存在差值，则返回差值与当前元素的索引
            if (j := hash_table.get(target - num)) is not None:
                return [j, i]

            # * 将当前元素及其索引存入哈希表
            hash_table[num] = i

        return []
