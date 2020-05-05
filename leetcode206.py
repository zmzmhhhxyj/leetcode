# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def showList(node):
    while node:
        print(node.val)
        node = node.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prevHead = None
        while head:
            nextNode = head.next
            head.next = prevHead
            prevHead = head
            head = nextNode
        return prevHead

    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return last
        
        
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
x = Solution()
res = x.reverseList2(n1)
showList(res)
