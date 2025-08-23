from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


def to_list(nums: List[int]) -> Optional[ListNode]:
    head = None

    for num in nums:
        node = ListNode(num, head)
        head = node

    return head


def to_array(head: Optional[ListNode]) -> List[int]:
    nums = []

    while head is not None:
        nums.append(head.val)
        head = head.next

    return nums
