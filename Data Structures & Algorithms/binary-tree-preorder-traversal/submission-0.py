# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,result):
          if root != None:
            result.append(root.val)
            helper(root.left,result)
            helper(root.right,result)  
            
        result = []
        helper(root,result)
        return result
        