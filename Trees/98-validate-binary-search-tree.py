# LeetCode 98 - Validate Binary Search Tree

# Approach:
# A valid BST must satisfy:
# left subtree values < root value < right subtree values.
#
# Use recursion with a valid range (lower, upper).
# Each node must lie within its allowed range.

class Solution(object):
    def isValidBST(self, root):
        def validate(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))


# Time Complexity: O(n)
# Space Complexity: O(h)
# h = height of the BST
