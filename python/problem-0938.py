"""
Problem 938 - Range Sum of BST

Given the root node of a binary search tree, return the sum of values of 
all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sumNodes = 0
        if L <= root.val <= R:
            sumNodes += root.val
        if root.left != None:
            sumNodes += self.rangeSumBST(root.left, L, R)
        if root.right != None:
            sumNodes += self.rangeSumBST(root.right, L, R)
        return sumNodes


if __name__ == "__main__":
    # 1st tree
    t1 = TreeNode(10)
    t1.left = TreeNode(5)
    t1.right = TreeNode(15)
    t1.left.left = TreeNode(3)
    t1.left.right = TreeNode(7)
    t1.right.right = TreeNode(18)

    # 2nd tree
    t2 = TreeNode(10)
    t2.left = TreeNode(5)
    t2.right = TreeNode(15)
    t2.left.left = TreeNode(3)
    t2.left.right = TreeNode(7)
    t2.right.left = TreeNode(13)
    t2.right.right = TreeNode(18)
    t2.left.left.right = TreeNode(6)

    print(Solution().rangeSumBST(t1, 7, 15))  # Should return 32
    print(Solution().rangeSumBST(t2, 6, 10))  # Should return 23
