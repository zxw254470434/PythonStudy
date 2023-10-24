from ListNode import *
from typing import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findFromEnd(head: ListNode, k: int) -> ListNode:
            p1 = head
            # p1 先走 k 步
            for i in range(k):
                p1 = p1.next
            p2 = head
            # p1 和 p2 同时走 n - k 步
            while p1 is not None:
                p2 = p2.next
                p1 = p1.next
            # p2 现在指向第 n - k + 1 个节点，即倒数第 k 个节点
            return p2

        # 虚拟头结点
        dummy = ListNode(-1)
        dummy.next = head
        # 删除倒数第 n 个，要先找倒数第 n + 1 个节点
        x = findFromEnd(dummy, n + 1)
        # 删掉倒数第 n 个节点
        x.next = x.next.next
        return dummy.next
