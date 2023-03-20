from ListNode import ListNode

l1 = None
for i in [3, 4, 2]:
    l1 = ListNode(i, l1)

l2 = None
for i in [4, 6, 5]:
    l2 = ListNode(i, l2)


class Solution_2:
    def addTwoNumbers(l1, l2):
        num1 = 0
        num2 = 0
        times = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                num1 += 10 ** times * l1.val
                l1 = l1.next
            if l2 is not None:
                num2 += 10 ** times * l2.val
                l2 = l2.next
            times += 1
        num3 = num1 + num2
        temp = ListNode(0)
        head = temp
        for i in reversed(str(num3)):
            temp.next = ListNode(int(i))
            temp = temp.next
        return head.next


result = Solution_2.addTwoNumbers(l1, l2)
head = result
while head is not None:
    print(head.val)
    head = head.next
