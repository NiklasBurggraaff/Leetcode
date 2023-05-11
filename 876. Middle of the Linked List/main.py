# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        middle = head

        while current != None:
            count += 1

            current = current.next

            if count % 2 == 0:
                middle = middle.next

        return middle
