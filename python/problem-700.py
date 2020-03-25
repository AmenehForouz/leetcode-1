# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        currNode = root
        
        while currNode != None:
            if val == currNode.val:
                return currNode
            elif val > currNode.val:
                currNode = currNode.right
            else:
                currNode = currNode.left
        
        return None