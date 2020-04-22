# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def constrcutList(l):
    if len(l)==0:
        return None
    dummy = ListNode(l[0])
    node = dummy
    i = 0
    for i in range(len(l)-1):
        # node = ListNode(l[i])
        node.next = ListNode(l[i+1])
        node = node.next
    return dummy

def showList(node):
    while node:
        print(node.val)
        node = node.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        node = dummyHead
        rest = 0
        while l1 or l2:
            if l1 and l2:
                num = l1.val+l2.val+rest
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                num = l2.val+rest
                l2 = l2.next
            elif not l2:
                num = l1.val+rest
                l1 = l1.next
            node.next = ListNode(num%10)
            rest = num//10
            node = node.next
        if rest==1:
            node.next = ListNode(1)
        return dummyHead.next
        
# l1 = constrcutList([2,4,3])
# l2 = constrcutList([5,6,4,9,6])
l1 = constrcutList([1])
l2 = constrcutList([9,9])
x = Solution()
ans = x.addTwoNumbers(l1,l2)
showList(ans)