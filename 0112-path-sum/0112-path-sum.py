# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node,my_sum):
            if not node:
                return False
            my_sum += node.val
            if not node.left and not node.right:
                return my_sum == targetSum

            return dfs(node.left, my_sum) or dfs(node.right, my_sum)
        
        return dfs(root, 0)