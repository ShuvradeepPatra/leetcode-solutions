# LeetCode 145 - Binary Tree Postorder Traversal

# Approach:
# Use recursion to traverse the tree in postorder.
# Postorder follows the order:
# Left -> Right -> Root
#
# For each node, recursively traverse the left subtree,
# then the right subtree, and finally add the node's value.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        def postorder(node):
            if node is None:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]
        return postorder(root)
