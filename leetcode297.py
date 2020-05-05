from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructBinaryTree(elemList):
    length = len(elemList)
    if(length == 0):
        return None
    _root = TreeNode(elemList[0])
    def recr(root, num):
        # num: number of node, start by 0 (root)
        leftNumber = 2*num+1
        rightNumber = 2*num+2
        if(leftNumber < length and elemList[leftNumber] != None):
            root.left = TreeNode(elemList[leftNumber])
            recr(root.left, leftNumber)
        else:
            root.left = None
        if(rightNumber < length and elemList[rightNumber] != None):
            root.right = TreeNode(elemList[rightNumber])
            recr(root.right, rightNumber)
        else:
            root.right = None
    recr(_root, 0)
    return _root

def levelOrder(root: TreeNode) :
    res, queue = [],deque([(root,0)])
    while queue:
        cur,level = queue.popleft()
        if cur:
            if len(res)<level+1:
                res.append([])
            res[level].append(cur.val)
            queue.append([cur.left,level+1])
            queue.append([cur.right,level+1])
    print(res)

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.shelper(root,res)
        return " ".join(res)
    
    def shelper(self,root,res):
        if not root:
            res.append("#")
            return
        res.append(str(root.val))
        self.shelper(root.left,res)
        self.shelper(root.right,res)
        return
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        root = self.dhelper(data,[0])
        return root
        
    def dhelper(self,data,pos):
        if data[pos[0]]=="#":
            pos[0] += 1
            return None
        node = TreeNode(int(data[pos[0]]))
        pos[0] += 1
        node.left = self.dhelper(data,pos)
        node.right = self.dhelper(data,pos)
        return node

tree = constructBinaryTree([1,2,3,None,None,4,5])
codec = Codec()
root = codec.deserialize(codec.serialize(tree))
levelOrder(root)