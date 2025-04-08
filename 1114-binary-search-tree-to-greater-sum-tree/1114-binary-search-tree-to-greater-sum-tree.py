# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 
            
            r_sum = dfs(node.right)
            self.my_sum += node.val
            node.val  = self.my_sum
            l_sum = dfs(node.left)

        
        self.my_sum = 0
        dfs(root)   
        return root