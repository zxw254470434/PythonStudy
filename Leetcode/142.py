from ListNode import *
from typing import *


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
