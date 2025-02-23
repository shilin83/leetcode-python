from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def arrayToList(nums: List[int]) -> Optional[ListNode]:
    head = None

    for i in range(len(nums) - 1, -1, -1):
        node = ListNode(nums[i], head)
        head = node

    return head


def listToArray(head: Optional[ListNode]) -> List[int]:
    result = []

    while head is not None:
        result.append(head.val)
        head = head.next

    return result
