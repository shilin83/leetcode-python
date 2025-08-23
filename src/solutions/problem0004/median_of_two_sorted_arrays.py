import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from helpers import MAX_INT32, MIN_INT32

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # * 确保 nums1 的长度小于等于 nums2 的长度
        m, n = len(nums1), len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # * low, high 分别表示 nums1 的左右边界
        low, high = 0, m

        # * nums1:  ……………… nums1[i-1] | nums1[i] ……………………
        # * nums2:  ……………… nums2[j-1] | nums2[j] ……………………
        while low <= high:
            # * i, j 分别表示 nums1 和 nums2 分割点
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            # * 获取分界线左右两侧的最大值和最小值
            max_left1 = MIN_INT32 if 0 == i else nums1[i - 1]
            min_right1 = MAX_INT32 if m == i else nums1[i]
            max_left2 = MIN_INT32 if 0 == j else nums2[j - 1]
            min_right2 = MAX_INT32 if n == j else nums2[j]

            # * 检查分割是否正确
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if 0 == (m + n) % 2:
                    # * 偶数个元素，返回中间两个数的平均值
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0

                # * 奇数个元素，返回左半部分的最大值
                return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # * nums1 中的分界线划多了，要向左边移动
                high = i - 1
            else:
                # * nums1 中的分界线划少了，要向右边移动
                low = i + 1

        return 0.0
