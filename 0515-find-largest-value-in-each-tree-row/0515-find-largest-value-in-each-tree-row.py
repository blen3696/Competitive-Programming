# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
  
        res = []
        def helper(node, d):
            if not node:
                return
            if d == len(res):
                res.append(node.val)  
            else:
                res[d] = max(res[d], node.val) 
            
            helper(node.left, d + 1)
            helper(node.right, d + 1)

        helper(root, 0)
        return res
