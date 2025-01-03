from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def int2List(nums: List[int]) -> Optional[ListNode]:
    length = len(nums)
    head = None

    if length != 0:
        for num in reversed(nums):
            node = ListNode(num, head)
            head = node

    return head
