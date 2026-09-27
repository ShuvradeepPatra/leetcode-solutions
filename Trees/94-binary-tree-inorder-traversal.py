# LeetCode 94 - Binary Tree Inorder Traversal

# Approach:
# Use recursion to traverse the tree in inorder.
# Inorder follows the order:
# Left -> Root -> Right
#
# For each node, recursively traverse the left subtree,
# then add the node's value, and finally traverse the right subtree.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        return inorder(root)
