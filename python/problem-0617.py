"""
Problem 617 - Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the 
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two 
nodes overlap, then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


# Preorder traversal
def showTree(t: TreeNode) -> List[int]:
    tree_list = []
    if t:
        tree_list.append(t.val)
        tree_list = tree_list + showTree(t.left)
        tree_list = tree_list + showTree(t.right)
    return tree_list


if __name__ == "__main__":
    # Tree t1
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)
    t1.right = TreeNode(2)

    # Tree t2
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)

    merged_tree = Solution().mergeTrees(t1, t2)
    print(showTree(merged_tree))  # Should return [3, 4, 5, 4, 5, 7]
