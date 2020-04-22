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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        preOdd = head
        preEven = preOdd.next
        evenHead = preEven
        while preEven and preEven.next:
            nextOdd = preEven.next
            nextEven = nextOdd.next
            preOdd.next = nextOdd
            preEven.next = nextEven
            nextOdd.next = evenHead
            if nextEven and nextEven.next:
                preEven = nextEven
                preOdd = nextOdd
            else:
                break
        return head
        
x = Solution()
node = constrcutList([1,2,3,4,5,6])
ans = x.oddEvenList(node)
showList(ans)