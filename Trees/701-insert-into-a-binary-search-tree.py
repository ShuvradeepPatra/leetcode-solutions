# LeetCode 701 - Insert into a Binary Search Tree

# Approach:
# If the tree is empty, create a new node with the given value.
# If val is smaller than the current node, insert it into the left subtree.
# Otherwise, insert it into the right subtree.
# Recursively continue until an empty position is found.

# Time Complexity: O(h)
# Space Complexity: O(h)
# h = height of the BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
