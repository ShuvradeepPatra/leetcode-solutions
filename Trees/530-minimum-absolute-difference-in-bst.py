# LeetCode 530 - Minimum Absolute Difference in BST

# Approach:
# Perform an inorder traversal of the BST.
# Inorder traversal visits BST nodes in sorted order.
# Therefore, the minimum absolute difference must be
# between two adjacent values in this traversal.

class Solution(object):
    def getMinimumDifference(self, root):
        prev = None
        min_diff = float('inf')

        def inorder(node):
            nonlocal prev, min_diff

            if not node:
                return

            inorder(node.left)

            if prev is not None:
                min_diff = min(min_diff, node.val - prev)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return min_diff


# Time Complexity: O(n)
# Space Complexity: O(h)
# h = height of the BST
