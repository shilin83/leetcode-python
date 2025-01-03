from typing import Optional

from src.structures.linkedList import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        current, carry = head, 0

        # * 遍历两个链表，计算每个节点的和，并与当前进位值相加
        # * 遍历结束后，如果还有进位值，则在链表末尾添加新的节点
        while l1 is not None or l2 is not None or carry != 0:
            sum = carry

            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next

            current.next = ListNode(sum % 10)
            current = current.next
            carry = sum // 10

        return head.next
