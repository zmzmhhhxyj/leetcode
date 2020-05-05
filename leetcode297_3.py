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
import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return " ".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split()
        q = collections.deque()
        root = TreeNode(int(data[0]))
        q.append(root)
        pos = 1
        while q:
            node = q.popleft()
            if data[pos] != "#":
                node.left = TreeNode(int(data[pos]))
                q.append(node.left)
            pos+=1
            if data[pos] != "#":
                node.right = TreeNode(int(data[pos]))
                q.append(node.right)
            pos+=1
        return root
            
tree = constructBinaryTree([1,2,3,None,None,4,5])
# tree = constructBinaryTree([])
codec = Codec()
root = codec.deserialize(codec.serialize(tree))
levelOrder(root)