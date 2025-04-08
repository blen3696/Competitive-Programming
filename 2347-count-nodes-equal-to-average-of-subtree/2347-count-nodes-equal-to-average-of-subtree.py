# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ctn = 0
        self.dfs(root)

        return self.ctn 

    def dfs(self, node):
        if not node:
            return (0,0)

        if not node.left and not node.right:
            self.ctn += 1
            return (node.val, 1)

        l_sum, l_ctn = self.dfs(node.left)
        r_sum, r_ctn = self.dfs(node.right)

        ave = (l_sum + r_sum + node.val)// (l_ctn + r_ctn + 1)

        if ave == node.val:
            self.ctn += 1

        return (l_sum + r_sum + node.val, l_ctn + r_ctn + 1 )