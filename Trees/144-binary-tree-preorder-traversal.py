# LeetCode 144 - Binary Tree Preorder Traversal

# Approach:
# Use recursion to traverse the tree in preorder.
# Preorder follows the order:
# Root -> Left -> Right
#
# For each node, first add the node's value,
# then recursively traverse the left subtree,
# and finally traverse the right subtree.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        def preorder(node):
            if node is None:
                return []
            return [node.val] + preorder(node.left) + preorder(node.right)
        return preorder(root)
