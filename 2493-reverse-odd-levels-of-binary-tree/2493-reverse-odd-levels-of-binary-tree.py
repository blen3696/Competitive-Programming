# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(left,right,l):
            if not left:
                return 
            if l%2 != 0:
                left.val,right.val = right.val, left.val
            helper(left.left,right.right,l+1)
            helper(left.right,right.left,l+1)
            
        helper(root.left,root.right,1)
        return root