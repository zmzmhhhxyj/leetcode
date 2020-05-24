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
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head,head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev,slow.next,slow = None,None,slow.next
        while slow:
            prev,slow.next,slow = slow,prev,slow.next
        while head and prev:
            if head.val==prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
        return True

l = constrcutList([34,2,3,1])
x = Solution()
res = x.isPalindrome(l)
print(res)