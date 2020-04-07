from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if not l2 else l2
        if l1.val>l2.val:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1

l10 = ListNode(1)
l11 = ListNode(2)
l12 = ListNode(5)
l10.next = l11
l11.next = l12

l20 = ListNode(1)
l21 = ListNode(3)
l22 = ListNode(4)
l20.next = l21
l21.next = l22

x = Solution()
res = x.mergeTwoLists(l10,l20)
print(res)