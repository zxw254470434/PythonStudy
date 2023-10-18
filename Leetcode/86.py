from ListNode import *
from typing import *


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(-1)
        grater_dummy = ListNode(-1)

        less = less_dummy
        grater = grater_dummy

        p = head

        while p:
            if p.val < x:
                less.next = p
                less = less.next
            else:
                grater.next = p
                grater = grater.next
            p = p.next

        less.next = grater_dummy.next
        grater.next = None

        return less_dummy.next
