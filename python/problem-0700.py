"""
Problem 700 - Search in a Binary Search Tree

Given the root node of a binary search tree (BST) and a value. You need to 
find the node in the BST that the node's value equals the given value. 
Return the subtree rooted with that node. If such node doesn't exist, you 
should return NULL.
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


# Preorder traversal
def showTree(t: TreeNode) -> List[int]:
    tree_list = []
    if t:
        tree_list.append(t.val)
        tree_list = tree_list + showTree(t.left)
        tree_list = tree_list + showTree(t.right)
    return tree_list


if __name__ == "__main__":
    # Create tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(7)
    val = 2
    print(showTree(Solution().searchBST(root, val)))  # Should return [2, 1, 3]
