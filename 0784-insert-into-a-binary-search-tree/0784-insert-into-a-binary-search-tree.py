# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node,val):
            if node is None:
                return TreeNode(val)
            if val < node.val:
                node.left = helper(node.left, val)
            else:
               node.right =  helper(node.right, val)
            return node
        return helper(root,val)