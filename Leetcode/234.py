from ListNode import *
from typing import *

class Solution:

    def __init__(self):
        self.left = None

    def traverse(self,right: ListNode) -> bool:
        if right is None:
            return True
        res = self.traverse(right.next)
        # 后序遍历代码
        res = res and (right.val == self.left.val)
        self.left = self.left.next
        return res

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        return self.traverse(head)
