"""
Problem 104 - Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the 
root node down to the farthest leaf node.
"""

from typing import List


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not (root.left or root.right):
            return 1
        elif root.left and not root.right:
            return 1 + self.maxDepth(root.left)
        elif not root.left and root.right:
            return 1 + self.maxDepth(root.right)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Preorder traversal
def showTree(t: TreeNode) -> List[int]:
    tree_list = []
    if t:
        tree_list.append(t.val)
        tree_list = tree_list + showTree(t.left)
        tree_list = tree_list + showTree(t.right)
    return tree_list

if __name__ == '__main__':
    root = TreeNode(val=3)
    root.left = TreeNode(val=9)
    root.right = TreeNode(val=20)
    root.right.left = TreeNode(val=15)
    root.right.right = TreeNode(val=7)

    # Should return 3
    print(Solution().maxDepth(root))

    root2 = TreeNode(val=1)
    root2.right = TreeNode(val=2)

    # Should return 2
    print(Solution().maxDepth(root2))