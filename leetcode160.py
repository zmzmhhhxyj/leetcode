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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa, pb = headA,headB
        len1, len2 = 0,0
        while pa:
            len1+=1
            pa = pa.next
        while pb:
            len2+=1
            pb = pb.next
        pa, pb = headA,headB
        if len1>len2:
            for i in range(len1-len2):
                pa = pa.next
        if len1<len2:
            for i in range(len2-len1):
                pb = pb.next
        while pa is not pb:
            pa = pa.next
            pb = pb.next
        return pa

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa, pb = headA,headB
        while pa is not pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa
        

x = Solution()
l1 = constrcutList([4,1])
l2 = constrcutList([5,0,1])
l3 = constrcutList([8,3,4])
l1.next.next = l3
l2.next.next.next = l3
ans = x.getIntersectionNode(l1,l2)
print(ans.val)