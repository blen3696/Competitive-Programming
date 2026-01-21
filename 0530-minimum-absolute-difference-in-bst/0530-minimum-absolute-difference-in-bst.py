# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_dif = float('inf')

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            if self.prev is not None:
                self.min_dif = min(self.min_dif,abs(self.prev - node.val))
            self.prev = node.val

            dfs(node.right)


        dfs(root)
        return self.min_dif
