# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        
        newTree = TreeNode(t1.val + t2.val)
        
        if t1.left == None:
            if t2.left == None:
                newTree.left = None
            else:
                newTree.left = t2.left
        else:
            if t2.left == None:
                newTree.left = t1.left
            else:
                newTree.left = self.mergeTrees(t1.left, t2.left)
        
        if t1.right == None:
            if t2.right == None:
                newTree.right = None
            else:
                newTree.right = t2.right
        else:
            if t2.right == None:
                newTree.right = t1.right
            else:
                newTree.right = self.mergeTrees(t1.right, t2.right)
        
        return newTree