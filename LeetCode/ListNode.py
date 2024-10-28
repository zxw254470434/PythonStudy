# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
前插法创建单链表
1、创建一个只有头节点 L 的空链表
2、根据待创建链表包括的元素个数 n ，循环 n 次以下操作
    a、生成一个新节点 p
    b、将元素值赋给新节点 p 的 val
    c、将新节点 p 插入到头节点 L 之后
注：需要按逆序输入数据
'''

L = ListNode(0)  # 创建一个只有头节点的单链表


def CreateList_H(L, n, nums):
    for i in range(0, n):
        p = ListNode(nums[i])
        p.next = L.next
        L.next = p


'''
尾插法创建单链表
1、创建一个只有头节点 L 的空链表
2、尾指针 r 初始化，指向 L
3、根据待创建链表包括的元素个数 n ，循环 n 次以下操作
    a、生成一个新节点 p
    b、将元素值赋给新节点 p 的 val
    c、将新节点 p 插入到尾指针 r 之后
    d、尾指针指向新的尾节点 p
'''

L = ListNode(0)  # 创建一个只有头节点的单链表


def CreateList_R(L, n, nums):
    r = L
    for i in range(0, n):
        p = ListNode(nums[i])
        r.next = p
        r = p
