from typing import Optional
from src.structures.LinkedList import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current, carry = head, 0

        while l1 is not None or l2 is not None or carry != 0:
            # * 计算当前节点的和
            sum = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry

            # * 移动到下一个节点
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            # * 创建新节点，值为 sum 除 10 取余
            current.next = ListNode(sum % 10)
            current = current.next

            # * 计算进位，值为 sum 除 10 取整
            carry = sum // 10

        return head.next
