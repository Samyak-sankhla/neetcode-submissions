# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_height(node):
            if node is None:
                return 0

            left_height = get_height(node.left)

            # Left subtree is already unbalanced
            if left_height == -1:
                return -1

            right_height = get_height(node.right)

            # Right subtree is already unbalanced
            if right_height == -1:
                return -1

            # Current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1

            # Height of the current subtree
            return 1 + max(left_height, right_height)

        return get_height(root) != -1