# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node,output):
            if node is None:
                return
            inorder(node.left,output)
            output.append(node.val)
            inorder(node.right,output)
        output=[]
        inorder(root,output)
        for i in range(1,len(output)):
            if output[i-1] >= output[i]:
                return False
        return True