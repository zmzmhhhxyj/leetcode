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
    def reorderList(self, head: ListNode) -> None:
        fast, slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre, slow.next, slow = None,None,slow.next
        # pre, slow, slow.next= None,slow.next,None
        # 这两句话居然是不一样的 神奇!
        while slow:
            slow.next,slow, pre = pre,slow.next,slow
        while head and pre:
            head.next, pre.next, head, pre = pre,head.next,head.next,pre.next


    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        tmp = slow.next
        slow.next = None
        slow = tmp
        while slow:
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        while head and pre:
            headNext = head.next
            preNext = pre.next
            head.next = pre
            pre.next = headNext
            head = headNext
            pre = preNext
        return 

x = Solution()
a = constrcutList([1,2,3,4,5])
x.reorderList(a)
showList(a)