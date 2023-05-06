from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head

        while current is not None:
            count += 1
            current = current.next

        return count

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = self.getLength(head)
        prev = None
        current = head

        split = (length + 1) // 2

        for i in range(length):
            if i >= split:
                next = current.next
                current.next = prev
                prev = current
                current = next
            else:
                prev = current
                current = current.next

        tail = prev

        for _ in range(length // 2):
            if head.val != tail.val:
                return False

            head = head.next
            tail = tail.next

        return True


def main():
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    head2 = ListNode(1, ListNode(2))

    print("[1,2,2,1]: " + str(Solution().isPalindrome(head1)))
    print("[1,2]: " + str(Solution().isPalindrome(head2)))


if __name__ == "__main__":
    main()
