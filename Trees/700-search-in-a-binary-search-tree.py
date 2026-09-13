# LeetCode 700 - Search in a Binary Search Tree

# Approach:
# If the current node is None, the value is not present.
# If the current node contains the target value, return the node.
# If val is smaller than the current node, search the left subtree.
# Otherwise, search the right subtree.
# This uses the Binary Search Tree property.

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
    def searchBST(self, root, val):
       if root is None:
        return None

       if val == root.val:
        return root

       if val < root.val:
        return self.searchBST(root.left, val)
       else:
        return self.searchBST(root.right, val)
