# LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

# Approach:
# Use the Binary Search Tree property.
# If both p and q are smaller than the current root,
# move to the left subtree.
# If both are greater than the current root,
# move to the right subtree.
# Otherwise, the current root is the Lowest Common Ancestor.

# Time Complexity: O(h)
# Space Complexity: O(1)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
