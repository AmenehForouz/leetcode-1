# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        combined_vals = self.preorder(root1) + self.preorder(root2)
        return sorted(combined_vals)
    
    def preorder(self, root: TreeNode) -> List[int]:
        vals = []
        if root:
            vals = self.preorder(root.left)
            vals = vals + self.preorder(root.right)
            vals.append(root.val)
        return vals