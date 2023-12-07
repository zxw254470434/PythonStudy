from ListNode import *
from typing import *


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # 如果链表为空，返回 null 。
            return None
        slow, fast = head, head
        while fast:  # 遍历链表，并找到重复元素。
            if fast.val != slow.val:  # 如果 fast 指向的节点与 slow 指向的节点的值不相等，说明链表中出现了重复元素。
                slow.next = fast  # 将 slow 指向 fast 的位置。
                slow = slow.next  # slow 指向下一个节点。
            fast = fast.next  # fast 指向下一个节点。
        slow.next = None  # 断开与后面重复元素的连接
        return head  # 返回处理后的链表头节点。
