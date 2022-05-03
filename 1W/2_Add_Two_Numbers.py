from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        str_l1, str_l2 = "", ""
        while l1:
            str_l1 += str(l1.val)
            l1 = l1.next
        while l2:
            str_l2 += str(l2.val)
            l2 = l2.next
        int_l1 = int(str_l1[::-1])
        int_l2 = int(str_l2[::-1])
        result = list(map(int, str(int_l1 + int_l2)[::-1]))

        for data in result:
            node = ListNode(data)
            if head is None:
                head = node
            else:
                temp = head
                while temp.next is not None:
                    temp = temp.next
                temp.next = node
        return head








