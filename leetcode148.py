#Sort a linked list in O(n log n) time using constant space complexity.

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head
        slow = head 
        fast = head
        end = None
        while fast is not None and fast.next is not None:
            end=slow
            slow=slow.next
            fast=fast.next.next
        end.next=None
        head1=self.sortList(head)
        head2=self.sortList(slow)
        newHead = merge(head1,head2)
        return newHead

def merge(head1,head2):
    newHead = Node(0)
    dummyNode = newHead
    while head1 is not None and head2 is not None:
        if head1.val<head2.val:
            newHead.next=head1
            head1=head1.next
            newHead=newHead.next
        else:
            newHead.next=head2
            head2=head2.next
            newHead=newHead.next
    if head1 is not None:
        newHead.next=head1
    if head2 is not None:
        newHead.next=head2
    return dummyNode.next

class LinkList(object):
    # 初始化
    def __init__(self):
        self.head = 0

    # 获取链表元素
    def __getitem__(self, key):
        if self.is_empty():
            print('linklist is empty.')
        elif (key <0)  or (key > self.getlength()):
            print('the given key is error')
        else:
            return self.getitem(key)

    # 设置元素
    def __setitem__(self, key, value):
        if self.is_empty():
            print('linklist is empty.')
        elif (key <0)  or (key > self.getlength()):
            print('the given key is error')
        else:
            self.delete(key)
            return self.insert(key)

    # 初始化列表
    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    # 获取链表长度
    def getlength(self):
        p =  self.head
        length = 0
        while p.next is not None:
            length+=1
            p = p.next
        return length
    
    # 判断链表是否为空
    def is_empty(self):
        if self.getlength() ==0:
            return True
        else:
            return False

    # 清空链表
    def clear(self):
        self.head = 0

    
    # 尾部追加节点
    def append(self,item):
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q

    # 
    def getitem(self,index):
        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head
        while p.next!=0 and j <index:
            p = p.next
            j+=1
        if j ==index:
            return p.val
        else:
            print ('target is not exist!')
    
    # 插入节点
    def insert(self,index,item):
        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p

     # 删除节点
    def delete(self,index):
        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            post.next = p.next
      
    # 寻找下标
    def index(self,value):
        if self.is_empty():
            print('Linklist is empty.')
            return
        p = self.head
        i = 0
        while p.next!=0 and not p.val ==value:
            p = p.next
            i+=1
        if p.val == value:
            return i
        else:
            return -1

l=LinkList()
l.initlist([-1,5,3,4,0])
x=Solution()
res=x.sortList(l.head)
lst=[]
while res is not None:
    lst.append(res.val)
    res=res.next
print(lst)