from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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

def outputBinaryTreeByDot(root):
    # generate graphviz file
    if(root == None):
        print ("receive None input")
        exit()
    head = ["digraph G{\n"]
    nodeSector = ["\n"]
    edgeSector = ["\n"]
    tail = ["\n}"]
    def recr(root, num):
        _str = 'node{0}[label = "{1}"];\n'.format(num, root.val)
        nodeSector.append(_str)
        if(root.left != None):
            edgeSector.append("node{0} -> node{1};\n".format(num, 2*num+1))
            recr(root.left, 2*num+1)
        if(root.right != None):
            edgeSector.append("node{0} -> node{1};\n".format(num, 2*num+2))
            recr(root.right, 2*num+2)
    recr(root, 0)
    return "".join(head) + "".join(nodeSector) + "".join(edgeSector) + "".join(tail)

def showDotFile(_strDotFile, _fileName = None, _outputName = None):
    import os
    if(_fileName != None):
        fileName = _fileName
    else:
        fileName = "tempBinaryTreeFile.dot"
    if(_outputName != None):
        outputName = _outputName
    else:
        outputName = "tempBinaryTreeFile.pdf"
    ##  save .dot file
    with open(fileName, "w") as fileHandler:
        fileHandler.write(_strDotFile)
    path = os.getcwd()
    ## command to generate grapg with graphviz
    cmd = "dot {0}\{1} -Tpdf -o {0}\{2}".format(path, fileName, outputName)
    print(cmd)
    consoleHandler = os.popen(cmd)
    print(consoleHandler.read())
    ## open PDF file
    print(os.popen("{0}\{1}".format(path, outputName)).read())

class Solution:
    #import system as sys
    import sys
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        self.maxHelper(root)
        return self.res
    
    def maxHelper(self,root):
        if not root:
            return 0
        l = max(0,self.maxHelper(root.left))
        r = max(0,self.maxHelper(root.right))
        self.res = max(root.val+l+r,self.res)
        return max(l,r)+root.val
        



tree = constructBinaryTree([-10,9,20,None,None,15,7])        
solution = Solution()
x = solution.maxPathSum(tree)
print(x)
