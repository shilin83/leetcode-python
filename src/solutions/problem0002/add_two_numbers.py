import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[2]))
from structures import ListNode

from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # * 创建虚拟头节点，作为结果链表的起点
        head = ListNode()

        current, carry = head, 0

        while l1 is not None or l2 is not None or carry != 0:
            # * 计算两个链表当前节点值与进位值的和
            sum = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            # * 创建新节点，并添加到结果链表
            current.next = ListNode(sum % 10)
            current = current.next

            # * 更新进位值
            carry = sum // 10

        return head.next
